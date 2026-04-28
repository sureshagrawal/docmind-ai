import { useEffect } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { Toaster } from "@/components/ui/sonner";

import { AuthProvider, useAuth } from "@/auth/AuthContext";
import { setAuthInterceptors } from "@/api/client";
import ProtectedRoute from "@/components/shared/ProtectedRoute";

import LoginPage from "@/components/auth/LoginPage";
import SignupPage from "@/components/auth/SignupPage";
import ForgotPasswordPage from "@/components/auth/ForgotPasswordPage";
import ResetPasswordPage from "@/components/auth/ResetPasswordPage";
import DashboardPage from "@/components/dashboard/DashboardPage";
import ResearchPage from "@/components/research/ResearchPage";
import AdminPage from "@/components/admin/AdminPage";

function AppRoutes() {
  const { accessToken, refresh, logout } = useAuth();

  useEffect(() => {
    setAuthInterceptors(
      () => accessToken,
      refresh,
      () => { logout(); }
    );
  }, [accessToken, refresh, logout]);

  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" replace />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/signup" element={<SignupPage />} />
      <Route path="/forgot-password" element={<ForgotPasswordPage />} />
      <Route path="/reset-password" element={<ResetPasswordPage />} />
      <Route path="/dashboard" element={<ProtectedRoute><DashboardPage /></ProtectedRoute>} />
      <Route path="/research" element={<ProtectedRoute><ResearchPage /></ProtectedRoute>} />
      <Route path="/admin" element={<AdminPage />} />
    </Routes>
  );
}

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <AppRoutes />
        <Toaster />
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
