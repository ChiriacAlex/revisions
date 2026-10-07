import { getPyLab } from "@/lib/content";
import { PyLab } from "./PyLab";

export function PyLabView({ id }: { id: string }) {
  const lab = getPyLab(id);
  if (!lab) return null;
  return <PyLab lab={lab} />;
}
