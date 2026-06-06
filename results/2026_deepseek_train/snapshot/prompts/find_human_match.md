You will be given a paper submission. Your job is to retrieve relevant human-written reviews from the human review dataset and use them as inspiration or grounding for weaknesses that plausibly apply to the current paper.

Rules:
- Only read files inside the human review directory. Do not open other files.
- Use multiple search queries (using file search tool) based on topic, method, setting, task, and likely failure modes. The exact file paths are provided to you separately.
- You should look for general concepts similarities and not specific details, as it is hard to retrieval highly similar articles
- Prefer a small number of highly relevant human reviews over many weak matches.
- Do not copy or paraphrase a human review point unless it genuinely fits the current paper.
- Do not invent strength/weaknesses just because they appeared in a retrieved review.
- If the retrieved reviews are not relevant enough, only return strength/weaknesses that are related, which could be empty. 
- Keep the search focused and efficient.
- Note in your final review that papers with similar strength/weaknesses's score range. List all similar paper path (not just shared weaknesses) for traceability.
- Do not made up an weakness and look for validation. Find similar papers and gather similar weaknesses.

Directory: Focus your search on the `human_reviews/` directory — that's where the human reviews live.

Input: The input paper's full content is provided inline in your context (between `--- PAPER CONTENT START ---` and `--- PAPER CONTENT END ---`). There is NO paper file on disk for you to open — read the paper directly from your context.

Tool workflow (all tools below operate ONLY on human review files, never on the input paper):
1. First inspect the input paper content that is already in your context.
2. `read_file(abs_path, start_line, end_line)` — read candidate human review files once you have selected them. Do NOT call this on the input paper (it is not a file).
3. `search_file(query, n, mode)` — BM25/Vector search to find the most relevant files in the human review directory. Use this to narrow down candidates.
4. `grep_file(pattern, abs_path)` — locate specific sections within a single candidate **human review** file. IMPORTANT: `grep_file` is ONLY for searching inside human review files. Do NOT use it to read or search the input paper — the paper is not on disk and is already fully visible in your context.

Process: 
1. Read the input paper directly from your context (between `--- PAPER CONTENT START ---` and `--- PAPER CONTENT END ---`) to identify the paper's core topic, method, and likely evaluation claims. Do not dump the whole paper into your visible answer. Do NOT try to open the paper as a file — it is not on disk.
2. Use `search_file` with several precise keyword combinations (topic, method, setting, task, likely failure modes) to find similar papers/reviews in the human review directory.
3. For the most relevant candidates, use `read_file` to read the human review files directly (reviews are short).
4. Extract weakness patterns that are concrete, specific, and transferable.
5. Write a strength/weaknesses review for the current paper.

Output requirements:
- Do not include your search process, intermediate notes, or dialogue outside the tag.
- Output only strength/weaknesses inside the tag.
- Keep each weakness specific to the current paper, not generic.
- For each weakness, it has to be mentioned or inspried by human reviews, do NOT write your review yourself. 
- If confidence is low, give fewer points (could be empty in some cases) rather than weak or speculative ones.
- For each weakness, include a quote to the retrivaled review that mentioned similar/same weakness or inspried your weakness finding
