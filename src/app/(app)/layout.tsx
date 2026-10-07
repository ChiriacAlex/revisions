import Link from "next/link";
import { requireSession } from "@/lib/auth/dal";
import { SessionTimer } from "@/components/SessionTimer";

export default async function AppLayout({ children }: { children: React.ReactNode }) {
  const { expiresAt } = await requireSession();
  return (
    <>
      <header className="topbar">
        <Link href="/" className="brand">
          <span className="brand-mark" aria-hidden>
            ∀
          </span>
          Révisions
        </Link>
        <span className="topbar-spacer" />
        <SessionTimer expiresAt={expiresAt.toISOString()} />
        <form action="/logout" method="post">
          <button type="submit" className="link-button">
            Déconnexion
          </button>
        </form>
      </header>
      {children}
    </>
  );
}
