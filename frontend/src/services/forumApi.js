import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000',
  withCredentials: true,
});

const handleRequest = async (request) => {
  try {
    const response = await request();
    return response.data;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

export const fetchCategories = () =>
  handleRequest(() => apiClient.get('/v1/categories'));

export const fetchQuestions = (skip = 0, limit = 10) =>
  handleRequest(() => apiClient.get('/v1/questions/', { params: { skip, limit } }));

export const fetchQuestionsByCategory = (categoryName, skip = 0, limit = 10) =>
  handleRequest(() => apiClient.get('/v1/questions/by-category/', { params: { category: categoryName, skip, limit } }));

export const fetchQuestionById = (questionId) =>
  handleRequest(() => apiClient.get(`/v1/questions/${questionId}`));

export const fetchAnswersByQuestionId = (questionId) =>
  handleRequest(() => apiClient.get('/v1/answers/by-question/', { params: { question_id: questionId } }));

export const createQuestion = (questionData) =>
  handleRequest(() => apiClient.post('/v1/questions/', questionData));

export const fetchTags = () =>
  handleRequest(() => apiClient.get('/v1/tags'));

export const createAnswer = (answerData) =>
  handleRequest(() => apiClient.post('/v1/answers/', answerData));