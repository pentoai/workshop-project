export interface BaseballPlayerInfo {
  history: string;
  simple_information: Record<string, any>;
  statistics: Record<string, any>;
  games: Array<Record<string, any>>;
}

export interface SearchResults {
  status: "idle" | "loading" | "success" | "error";
  streamText: string;
  playerData: BaseballPlayerInfo | null;
  error?: string;
}
