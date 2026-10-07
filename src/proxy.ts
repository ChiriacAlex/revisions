import { NextResponse, type NextRequest } from "next/server";
import { SESSION_COOKIE, verifySessionToken } from "@/lib/auth/session";

/** Premier filtre : toute page sans session valide (PIN saisi il y a moins d'1 h) part vers /login. */
export async function proxy(request: NextRequest) {
  const { pathname, search } = request.nextUrl;
  if (pathname === "/login" || pathname === "/login/") return NextResponse.next();

  const secret = process.env.SESSION_SECRET ?? "";
  let valid = false;
  try {
    valid = (await verifySessionToken(request.cookies.get(SESSION_COOKIE)?.value, secret)).valid;
  } catch {
    valid = false;
  }
  if (valid) return NextResponse.next();

  const login = new URL("/login/", request.url);
  if (pathname !== "/") login.searchParams.set("next", pathname + search);
  const response = NextResponse.redirect(login);
  response.cookies.delete(SESSION_COOKIE);
  return response;
}

export const config = {
  // Tout passe par le proxy, sauf les fichiers techniques de Next et les polices/CSS KaTeX publiques.
  matcher: ["/((?!_next/static|_next/image|favicon.ico|vendor/|robots.txt).*)"],
};
