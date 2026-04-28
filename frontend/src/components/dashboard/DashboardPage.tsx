import { useAuth } from "@/auth/AuthContext";
import { Button } from "@/components/ui/button";
import DocumentPanel from "@/components/documents/DocumentPanel";
import { LogOut } from "lucide-react";
import { useNavigate } from "react-router-dom";

export default function DashboardPage() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = async () => {
    await logout();
    navigate("/login");
  };

  return (
    <div className="flex h-screen bg-neutral-50">
      {/* Left Sidebar — Phase 4 will add chat sessions */}
      <aside className="w-64 border-r border-neutral-200 bg-white p-4 flex flex-col">
        <h1 className="text-lg font-semibold text-primary mb-6">DocMind AI</h1>
        <div className="flex-1">
          <p className="text-sm text-muted-foreground">Chat sessions (Phase 4)</p>
        </div>
        <div className="border-t border-neutral-200 pt-3 mt-3">
          <p className="text-xs text-muted-foreground truncate mb-2">{user?.email}</p>
          <Button variant="ghost" size="sm" className="w-full justify-start gap-2" onClick={handleLogout}>
            <LogOut className="h-4 w-4" />
            Sign out
          </Button>
        </div>
      </aside>

      {/* Center — Phase 4 will add chat window */}
      <main className="flex-1 flex items-center justify-center">
        <p className="text-muted-foreground">Select a chat or start a new one (Phase 4)</p>
      </main>

      {/* Right Panel — Documents */}
      <aside className="w-80 border-l border-neutral-200 bg-white p-4">
        <DocumentPanel />
      </aside>
    </div>
  );
}
