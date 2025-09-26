"use client";

import type { SearchResults } from "@/types/player";

interface PlayerResultsProps {
  results: SearchResults;
}

export default function PlayerResults({ results }: PlayerResultsProps) {
  const { status, streamText, playerData, error } = results;

  // Idle state
  if (status === "idle") {
    return (
      <div className="text-center py-12">
        <div className="w-16 h-16 bg-gray-100 dark:bg-gray-700 rounded-full flex items-center justify-center mx-auto mb-4">
          <span className="text-2xl">⚾</span>
        </div>
        <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">
          Ready to Search
        </h3>
        <p className="text-gray-500 dark:text-gray-400">
          Enter a baseball player's name to get started
        </p>
      </div>
    );
  }

  // Error state
  if (status === "error") {
    return (
      <div className="text-center py-12">
        <div className="w-16 h-16 bg-red-100 dark:bg-red-900 rounded-full flex items-center justify-center mx-auto mb-4">
          <span className="text-2xl">❌</span>
        </div>
        <h3 className="text-lg font-medium text-red-900 dark:text-red-100 mb-2">
          Search Failed
        </h3>
        <p className="text-red-600 dark:text-red-400 mb-4">
          {error || "An unexpected error occurred"}
        </p>
        {streamText && (
          <div className="mt-4 text-left">
            <h4 className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              Partial Response:
            </h4>
            <div className="bg-gray-50 dark:bg-gray-700 p-3 rounded-lg text-sm text-gray-600 dark:text-gray-300 whitespace-pre-wrap max-h-32 overflow-y-auto">
              {streamText}
            </div>
          </div>
        )}
      </div>
    );
  }

  // Loading state
  if (status === "loading") {
    return (
      <div className="space-y-4">
        <div className="flex items-center gap-3 text-blue-600 dark:text-blue-400">
          <div className="w-5 h-5 border-2 border-blue-600 border-t-transparent rounded-full animate-spin"></div>
          <span className="font-medium">Searching...</span>
        </div>

        {streamText && (
          <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
            <h4 className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              Live Updates:
            </h4>
            <div className="text-sm text-gray-600 dark:text-gray-300 whitespace-pre-wrap max-h-40 overflow-y-auto">
              {streamText}
            </div>
          </div>
        )}
      </div>
    );
  }

  // Success state with player data
  if (status === "success" && playerData) {
    return (
      <div className="space-y-6">
        {/* Player Basic Info */}
        {playerData.simple_information && (
          <div className="bg-gradient-to-r from-blue-50 to-orange-50 dark:from-blue-900/20 dark:to-orange-900/20 p-4 rounded-lg">
            <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-3">
              Baseball Legend
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-sm">
              {Object.entries(playerData.simple_information).map(
                ([key, value]) => (
                  <div key={key} className="flex justify-between">
                    <span className="font-medium text-gray-600 dark:text-gray-300 capitalize">
                      {key.replace(/_/g, " ")}:
                    </span>
                    <span className="text-gray-900 dark:text-white">
                      {String(value)}
                    </span>
                  </div>
                )
              )}
            </div>
          </div>
        )}

        {/* Career Summary */}
        {playerData.history && (
          <div className="bg-orange-50 dark:bg-orange-900/20 p-4 rounded-lg">
            <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-3 flex items-center gap-2">
              <span>📖</span>
              Career Summary
            </h3>
            <div className="text-gray-700 dark:text-gray-300 text-sm leading-relaxed">
              {playerData.history}
            </div>
          </div>
        )}

        {/* Statistics */}
        {playerData.statistics && (
          <div className="bg-green-50 dark:bg-green-900/20 p-4 rounded-lg">
            <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-3 flex items-center gap-2">
              <span>📊</span>
              Career Statistics
            </h3>
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 text-sm">
              {Object.entries(playerData.statistics).map(([key, value]) => (
                <div
                  key={key}
                  className="bg-white dark:bg-gray-800 p-3 rounded-lg text-center"
                >
                  <div className="font-bold text-lg text-gray-900 dark:text-white">
                    {String(value)}
                  </div>
                  <div className="text-gray-600 dark:text-gray-400 capitalize text-xs">
                    {key.replace(/_/g, " ")}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Games */}
        {playerData.games &&
          Array.isArray(playerData.games) &&
          playerData.games.length > 0 && (
            <div className="bg-purple-50 dark:bg-purple-900/20 p-4 rounded-lg">
              <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-3 flex items-center gap-2">
                <span>🏟️</span>
                Notable Games ({playerData.games.length})
              </h3>
              <div className="space-y-3 max-h-60 overflow-y-auto">
                {playerData.games
                  .slice(0, 5)
                  .map((game: any, index: number) => (
                    <div
                      key={index}
                      className="bg-white dark:bg-gray-800 p-3 rounded-lg"
                    >
                      <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-sm">
                        {Object.entries(game).map(([key, value]) => (
                          <div key={key} className="flex justify-between">
                            <span className="font-medium text-gray-600 dark:text-gray-300 capitalize">
                              {key.replace(/_/g, " ")}:
                            </span>
                            <span className="text-gray-900 dark:text-white">
                              {String(value)}
                            </span>
                          </div>
                        ))}
                      </div>
                    </div>
                  ))}
                {playerData.games.length > 5 && (
                  <p className="text-center text-gray-500 dark:text-gray-400 text-sm">
                    And {playerData.games.length - 5} more games...
                  </p>
                )}
              </div>
            </div>
          )}

        {/* Raw Stream Data (collapsible) */}
        {streamText && (
          <details className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
            <summary className="cursor-pointer font-medium text-gray-700 dark:text-gray-300 text-sm">
              View Raw Response
            </summary>
            <div className="mt-3 text-xs text-gray-600 dark:text-gray-400 whitespace-pre-wrap max-h-40 overflow-y-auto">
              {streamText}
            </div>
          </details>
        )}
      </div>
    );
  }

  // Fallback
  return (
    <div className="text-center py-12">
      <div className="w-16 h-16 bg-gray-100 dark:bg-gray-700 rounded-full flex items-center justify-center mx-auto mb-4">
        <span className="text-2xl">❓</span>
      </div>
      <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">
        No Results
      </h3>
      <p className="text-gray-500 dark:text-gray-400">
        No player data available
      </p>
    </div>
  );
}
