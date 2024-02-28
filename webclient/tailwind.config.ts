import { join } from "path";
import type { Config } from "tailwindcss";

import { skeleton } from "@skeletonlabs/tw-plugin";

const config = {
  darkMode: "class",
  content: [
    "./src/**/*.{html,js,svelte,ts}",
    join(
      require.resolve("@skeletonlabs/skeleton"),
      "../**/*.{html,js,svelte,ts}",
    ),
  ],
  theme: {
    extend: {},
  },
  plugins: [
    // Append the Skeleton plugin after other plugins
    skeleton({
      themes: { preset: [{ name: "hamlindigo", enhancements: true }] },
    }),
  ],
} satisfies Config;

export default config;