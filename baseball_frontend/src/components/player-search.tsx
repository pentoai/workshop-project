"use client";

import { useState } from "react";
import type { SearchResults } from "@/types/player";

interface PlayerSearchProps {
  onSearch: (results: SearchResults) => void;
}

export default function PlayerSearch({ onSearch }: PlayerSearchProps) {
  const [playerName, setPlayerName] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!playerName.trim()) {
      return;
    }

    setIsLoading(true);
    onSearch({
      status: "loading",
      streamText: "",
      playerData: null,
    });

    try {
      const response = await fetch(
        `http://localhost:8000/query?player_full_name=${encodeURIComponent(
          playerName.trim()
        )}`,
        {
          method: "GET",
          headers: {
            Accept: "text/event-stream",
          },
        }
      );

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const reader = response.body?.getReader();
      if (!reader) {
        throw new Error("Failed to get response reader");
      }

      let streamText = "";
      let lastJsonChunk = "";

      while (true) {
        const { done, value } = await reader.read();

        if (done) break;

        const chunk = new TextDecoder().decode(value);
        streamText += chunk;

        // Update the streaming text display
        onSearch({
          status: "loading",
          streamText,
          playerData: null,
        });

        // Try to extract JSON from the stream
        try {
          // Look for JSON object in the stream - find the first { and try to parse from there
          const firstBraceIndex = streamText.indexOf("{");
          if (firstBraceIndex !== -1) {
            const jsonCandidate = streamText.substring(firstBraceIndex).trim();
            try {
              const parsed = JSON.parse(jsonCandidate);
              // If parsing succeeds, this is our JSON data
              lastJsonChunk = jsonCandidate;
            } catch {
              // JSON might be incomplete, continue reading
            }
          }
        } catch {
          // Continue reading
        }
      }

      // Final attempt to parse JSON
      if (lastJsonChunk) {
        try {
          const playerData = JSON.parse(lastJsonChunk);
          onSearch({
            status: "success",
            streamText,
            playerData,
          });
        } catch (parseError) {
          console.error("Failed to parse final JSON:", parseError);
          onSearch({
            status: "error",
            streamText,
            playerData: null,
            error: "Failed to parse player data",
          });
        }
      } else {
        // Try one more time to find JSON in the complete stream
        const firstBraceIndex = streamText.indexOf("{");
        if (firstBraceIndex !== -1) {
          const jsonCandidate = streamText.substring(firstBraceIndex).trim();
          try {
            const playerData = JSON.parse(jsonCandidate);
            onSearch({
              status: "success",
              streamText,
              playerData,
            });
          } catch (parseError) {
            console.error(
              "Failed to parse JSON from complete stream:",
              parseError
            );
            onSearch({
              status: "error",
              streamText,
              playerData: null,
              error: "Failed to parse player data",
            });
          }
        } else {
          onSearch({
            status: "error",
            streamText,
            playerData: null,
            error: "No player data received",
          });
        }
      }
    } catch (error) {
      console.error("Search error:", error);
      onSearch({
        status: "error",
        streamText: "",
        playerData: null,
        error:
          error instanceof Error ? error.message : "An unknown error occurred",
      });
    } finally {
      setIsLoading(false);
    }
  };

  const handleClear = () => {
    setPlayerName("");
    onSearch({
      status: "idle",
      streamText: "",
      playerData: null,
    });
  };

  return (
    <div className="space-y-4">
      <form onSubmit={handleSearch} className="space-y-4">
        <div>
          <label
            htmlFor="player-name"
            className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
          >
            Player Full Name
          </label>
          <input
            id="player-name"
            type="text"
            value={playerName}
            onChange={(e) => setPlayerName(e.target.value)}
            placeholder="e.g., Gary Carter, Babe Ruth, Willie Mays"
            className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent bg-white dark:bg-gray-700 text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-gray-400"
            disabled={isLoading}
          />
        </div>

        <div className="flex gap-3">
          <button
            type="submit"
            disabled={isLoading || !playerName.trim()}
            className="flex-1 bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 disabled:from-gray-400 disabled:to-gray-500 text-white font-medium py-3 px-6 rounded-lg transition-all duration-200 disabled:cursor-not-allowed flex items-center justify-center gap-2"
          >
            {isLoading ? (
              <>
                <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                Searching...
              </>
            ) : (
              <>
                <span>🔍</span>
                Search
              </>
            )}
          </button>

          <button
            type="button"
            onClick={handleClear}
            disabled={isLoading}
            className="px-4 py-3 border border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 rounded-lg transition-colors disabled:cursor-not-allowed"
          >
            Clear
          </button>
        </div>
      </form>

      <div className="text-xs text-gray-500 dark:text-gray-400 bg-gray-50 dark:bg-gray-700 p-3 rounded-lg">
        <p className="font-medium mb-1">💡 Try searching for:</p>
        <ul className="list-disc list-inside space-y-1">
          <li>Hall of Fame players: Gary Carter, Babe Ruth, Willie Mays</li>
          <li>Modern stars: Mike Trout, Mookie Betts, Aaron Judge</li>
          <li>Use full names for best results</li>
        </ul>
      </div>
    </div>
  );
}
