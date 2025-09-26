# Know Your Player - Baseball Frontend

A modern Next.js application for querying comprehensive baseball player information. This frontend connects to the Baseball Backend API to provide detailed statistics, career highlights, and player information from America's baseball history.

![Know Your Player](https://img.shields.io/badge/Next.js-15.5-black?logo=next.js)
![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-4-38bdf8?logo=tailwindcss)

## Features

- 🔍 **Real-time Search**: Search for baseball players by full name
- 📊 **Live Streaming**: Watch the search progress with live updates
- 📈 **Comprehensive Data**: View detailed statistics, career history, and game information
- 🎨 **Modern UI**: Beautiful, responsive design with dark mode support
- ⚡ **Fast Performance**: Built with Next.js 15 and optimized for speed

## Prerequisites

- Node.js 18+
- Baseball Backend API running on `http://localhost:8000`

## Getting Started

1. **Install Dependencies**

   ```bash
   npm install
   ```

2. **Start Development Server**

   ```bash
   npm run dev
   ```

3. **Open Application**
   Open [http://localhost:3000](http://localhost:3000) in your browser

## Usage

1. **Enter Player Name**: Type the full name of a baseball player (e.g., "Gary Carter", "Babe Ruth")
2. **Search**: Click the search button to query the backend API
3. **Watch Progress**: See live updates as the system gathers information
4. **View Results**: Explore comprehensive player data including:
   - Basic information (birth date, positions, etc.)
   - Career summary and highlights
   - Detailed statistics
   - Notable games

## API Integration

The frontend connects to the Baseball Backend API at `http://localhost:8000/query` with the following features:

- **Streaming Response**: Real-time updates during data gathering
- **Error Handling**: Graceful handling of API errors and timeouts
- **JSON Parsing**: Automatic extraction of player data from stream

## Tech Stack

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript 5
- **Styling**: Tailwind CSS 4
- **State Management**: React useState hooks
- **API**: Fetch with streaming support
- **Linting**: Biome

## Project Structure

```
src/
├── app/
│   ├── layout.tsx          # Root layout with metadata
│   ├── page.tsx            # Main application page
│   └── globals.css         # Global styles
├── components/
│   ├── player-search.tsx   # Search input component
│   └── player-results.tsx  # Results display component
└── types/
    └── player.ts           # TypeScript type definitions
```

## Development

- **Linting**: `npm run lint`
- **Formatting**: `npm run format`
- **Type Checking**: Built into Next.js dev server

## Environment

- **Development**: http://localhost:3000
- **API Endpoint**: http://localhost:8000
- **CORS**: Enabled for cross-origin requests

## Examples

Try searching for these baseball legends:

- Gary Carter (Hall of Fame catcher)
- Babe Ruth (The Sultan of Swat)
- Willie Mays (The Say Hey Kid)
- Mike Trout (Modern superstar)
- Mookie Betts (Current star player)
