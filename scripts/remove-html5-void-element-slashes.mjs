import { readdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";

const root = path.resolve(".hugo/public");
const voidElement = /(<(?:area|base|br|col|embed|hr|img|input|link|meta|source|track|wbr)\b[^>]*?)\s*\/>/gi;

async function normalize(directory) {
	for (const entry of await readdir(directory, { withFileTypes: true })) {
		const filePath = path.join(directory, entry.name);

		if (entry.isDirectory()) {
			await normalize(filePath);
		} else if (entry.isFile() && entry.name.endsWith(".html")) {
			const html = await readFile(filePath, "utf8");
			const normalizedHtml = html.replace(voidElement, "$1>");

			if (normalizedHtml !== html) {
				await writeFile(filePath, normalizedHtml);
			}
		}
	}
}

await normalize(root);
