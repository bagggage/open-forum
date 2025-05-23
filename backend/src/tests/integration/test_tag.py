import pytest

class TestTag:
    tag_id = None

    @pytest.mark.order(4)
    @pytest.mark.asyncio
    async def test_get_tags(self, async_client):
        response = await async_client.get("/v1/tags/")

        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.order(3)
    @pytest.mark.asyncio
    async def test_create_tag(self, async_client):
        tag_data = {"name": "test_tag"}

        response = await async_client.post(
            "/v1/tags/",
            json=tag_data
        )

        assert response.status_code == 200
        TestTag.tag_id = response.json()["id"]

    @pytest.mark.order(12)
    @pytest.mark.asyncio
    async def test_get_tag(self, async_client):
        assert TestTag.tag_id is not None

        response = await async_client.get(f"/v1/tags/{TestTag.tag_id}")

        assert response.status_code == 200

    @pytest.mark.order(19)
    @pytest.mark.asyncio
    async def test_delete_tag(self, async_client):
        assert TestTag.tag_id is not None

        response = await async_client.delete(f"/v1/tags/{TestTag.tag_id}")

        assert response.status_code == 200
