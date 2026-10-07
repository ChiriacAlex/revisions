import { getItem } from "@/lib/content";
import { QcmItem } from "./QcmItem";
import { NumericItem } from "./NumericItem";
import { TrueFalseItem } from "./TrueFalseItem";

export function ItemView({ id }: { id: string }) {
  const item = getItem(id);
  if (!item) return null;
  switch (item.type) {
    case "qcm":
      return <QcmItem item={item} />;
    case "numeric":
      return <NumericItem item={item} />;
    case "truefalse":
      return <TrueFalseItem item={item} />;
  }
}
