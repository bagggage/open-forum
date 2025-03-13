import pytest

class TestAnswer:
    answer_id = None
    
    @pytest.mark.order(9)
    @pytest.mark.asyncio
    async def test_get_answers(self, async_client):
        response = await async_client.get("/v1/answers/")

        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.order(8)
    @pytest.mark.asyncio
    async def test_create_answer(self, async_client, auth_cookie):
        assert hasattr(pytest, "question_id")
        question_id = pytest.question_id

        answer_data = {
            "text": "This is a test answer",
            "question_id": question_id
        }

        response = await async_client.post(
            "/v1/answers/",
            json=answer_data,
            cookies=auth_cookie
        )

        assert response.status_code == 200
        TestAnswer.answer_id = response.json()["id"]

    @pytest.mark.order(13)
    @pytest.mark.asyncio
    async def test_get_answer(self, async_client):
        assert TestAnswer.answer_id is not None

        response = await async_client.get(f"/v1/answers/{TestAnswer.answer_id}")

        assert response.status_code == 200

    @pytest.mark.order(14)
    @pytest.mark.asyncio
    async def test_get_answers_by_question(self, async_client):
        assert hasattr(pytest, "question_id")
        question_id = pytest.question_id

        response = await async_client.get(f"/v1/answers/by-question/?question_id={question_id}")

        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.order(16)
    @pytest.mark.asyncio
    async def test_delete_answer(self, async_client):
        assert TestAnswer.answer_id is not None

        response = await async_client.delete(f"/v1/answers/{TestAnswer.answer_id}")

        assert response.status_code == 200
