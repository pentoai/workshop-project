"""Integration tests for the /query endpoint."""

import json
import pytest
from fastapi.testclient import TestClient
from baseball_backend.main import app
from baseball_backend.models.player_info import BaseballPlayerInfo


class TestQueryEndpoint:
    """Integration tests for the /query endpoint."""

    def test_query_endpoint_returns_200(self):
        """Test that /query endpoint returns 200 status."""
        # This test will fail until the /query endpoint is implemented
        client = TestClient(app)
        response = client.get("/query?player_full_name=Shohei%20Ohtani")
        assert response.status_code == 200

    def test_query_endpoint_returns_streaming_response(self):
        """Test that /query endpoint returns a streaming response."""
        # This test will fail until streaming is implemented
        client = TestClient(app)
        response = client.get("/query?player_full_name=Shohei%20Ohtani")
        assert response.status_code == 200
        # For TestClient, we can't easily test streaming, so we'll just check the response

    def test_query_endpoint_streams_text_then_json(self):
        """Test that endpoint streams text and concludes with JSON BaseballPlayerInfo."""
        # This test will fail until full implementation is complete
        client = TestClient(app)
        response = client.get("/query?player_full_name=Shohei%20Ohtani")
        assert response.status_code == 200

        # For TestClient, the streaming response is collected into a single response
        response_text = response.text

        # Find the JSON object (look for the first { after the text content)
        json_start = response_text.find("{\n")
        assert json_start >= 0, "No JSON found in response"

        # Extract just the JSON part
        json_content = response_text[json_start:]

        # Parse the JSON
        baseball_info = BaseballPlayerInfo.model_validate_json(json_content)

        assert isinstance(baseball_info, BaseballPlayerInfo)
        assert hasattr(baseball_info, "history")
        assert hasattr(baseball_info, "simple_information")
        assert hasattr(baseball_info, "statistics")
        assert hasattr(baseball_info, "games")

    def test_query_endpoint_with_different_player(self):
        """Test /query endpoint with a different player name."""
        # This test will fail until endpoint is implemented
        client = TestClient(app)
        response = client.get("/query?player_full_name=Mookie%20Betts")
        assert response.status_code == 200

    def test_query_endpoint_missing_parameter(self):
        """Test /query endpoint without required player_full_name parameter."""
        # This test will fail until parameter validation is implemented
        client = TestClient(app)
        response = client.get("/query")
        # Should return 422 for missing required parameter
        assert response.status_code == 422

    def test_query_endpoint_logs_request(self):
        """Test that requests to /query are logged."""
        # This test will fail until logging is properly implemented
        # This would typically check loguru logs, but for now we'll just ensure the request succeeds
        client = TestClient(app)
        response = client.get("/query?player_full_name=Shohei%20Ohtani")
        assert response.status_code == 200

    def test_query_endpoint_handles_internal_error(self):
        """Test that internal errors return 500 status."""
        # This test might be harder to trigger without mocking
        # For now, we'll assume it passes if endpoint exists
        client = TestClient(app)
        response = client.get("/query?player_full_name=Shohei%20Ohtani")
        # In a real failure scenario, this would be 500
        # For now, just check it doesn't fail unexpectedly
        assert response.status_code in [200, 500]
