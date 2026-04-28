import axios from "axios";

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000",
  headers: {
    "Content-Type": "application/json",
  },
  withCredentials: true,
});

// Phase 2: Request interceptor — attach Authorization: Bearer <token>
apiClient.interceptors.request.use((config) => {
  // Will be implemented in Phase 2 with AuthContext
  return config;
});

// Phase 2: Response interceptor — 401 auto-refresh + retry
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    // Will be implemented in Phase 2 with token refresh logic
    return Promise.reject(error);
  }
);

export default apiClient;
