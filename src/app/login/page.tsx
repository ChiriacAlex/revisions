import type { Metadata } from "next";
import { LoginForm } from "./LoginForm";
import { safeNextPath } from "@/lib/auth/redirect";

export const metadata: Metadata = { title: "Connexion" };

export default async function LoginPage({
  searchParams,
}: {
  searchParams: Promise<{ next?: string }>;
}) {
  const { next } = await searchParams;
  return (
    <main className="login-screen">
      <LoginForm next={safeNextPath(next)} />
    </main>
  );
}
