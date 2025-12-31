// services/api.js
import axios from "axios";

// Create an Axios instance with base URL
const api = axios.create({
  baseURL: "http://localhost:8000", // replace with your FastAPI backend URL
  headers: {
    "Content-Type": "application/json",
  },
});

// Optional: Interceptors for logging errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error("API Error:", error.response || error.message);
    return Promise.reject(error);
  }
);

export default api;

