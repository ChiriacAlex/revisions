/** N'autorise que les chemins internes (évite les redirections ouvertes vers un autre site). */
export function safeNextPath(raw: unknown): string {
  if (typeof raw !== "string") return "/";
  if (!raw.startsWith("/") || raw.startsWith("//") || raw.startsWith("/\\")) return "/";
  if (raw.startsWith("/login") || raw.startsWith("/logout")) return "/";
  return raw;
}
