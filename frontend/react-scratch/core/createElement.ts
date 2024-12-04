import { AnyProps, FunctionalComponent, ReactComponentExternalMetadata, ReactComponentInternalMetadata } from "./type";

export const createElement = <T extends AnyProps>(
  comopnent: ReactComponentExternalMetadata<T>["component"],
  props: T,
  ...children: Array<ReactComponentInternalMetadata>
): ReactComponentInternalMetadata => ({
  component: mapComponentToTaggedUnion(externalMeatadata.component),
  children: externalMetadata.children,
  props: externalMetadata.props,
  id: crypto.randomUUID(),
});