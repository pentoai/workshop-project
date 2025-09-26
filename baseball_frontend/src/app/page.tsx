"use client";

import { useState } from "react";
import PlayerSearch from "@/components/player-search";
import PlayerResults from "@/components/player-results";
import type { SearchResults } from "@/types/player";

export default function Home() {
  const [searchResults, setSearchResults] = useState<SearchResults>({
    status: "idle",
    streamText: "",
    playerData: null,
  });

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-orange-50 dark:from-gray-900 dark:to-gray-800">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-4xl md:text-6xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-orange-600 mb-4">
            Know Your Player
          </h1>
          <p className="text-lg text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
            Discover detailed baseball statistics, career highlights, and player
            information from the rich history of America's pastime.
          </p>
        </div>

        {/* Main Content */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 max-w-7xl mx-auto">
          {/* Search Panel */}
          <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6">
            <div className="flex items-center gap-3 mb-6">
              <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-blue-600 rounded-lg flex items-center justify-center">
                <span className="text-white text-xl">⚾</span>
              </div>
              <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
                Search Player
              </h2>
            </div>
            <PlayerSearch onSearch={setSearchResults} />
          </div>

          {/* Results Panel */}
          <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6">
            <div className="flex items-center gap-3 mb-6">
              <div className="w-10 h-10 bg-gradient-to-r from-orange-500 to-red-500 rounded-lg flex items-center justify-center">
                <span className="text-white text-xl">📊</span>
              </div>
              <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
                Results
              </h2>
            </div>
            <PlayerResults results={searchResults} />
          </div>
        </div>
      </div>
    </div>
  );
}
