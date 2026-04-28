Use comparative scoring to calibrate your final score.

How retrieval works: you do not have direct search tools for the human-review corpus. Use the `calibration_search` tool for every retrieval. It runs BM25 / vector search / grep internally and returns a list of paper paths with one-sentence summaries. You decide what to look for; it does the looking.

Workflow for every calibration step below:
1. Decide what you want to retrieve (topic, weakness pattern, strength pattern, score range, etc.).
2. Call `calibration_search` with a short natural-language request describing what you want.
3. Read the returned paper list. If you want more detail on a specific anchor, use your own read_file on the returned absolute path.

Do not try to call search_file, grep_file, or the BM25/vector index directly — those are only available inside `calibration_search`. If you want more or different anchors, call `calibration_search` again with a refined request.

&& IMPORTANT: Do NOT be afraid to be harsh/nice if the founded paper supports it. 

Your calibration process:

1. Topic-based anchors: ask `calibration_search` for papers with similar topics. Note their human scores.

2. Quality-based anchors: this is critical. Do not only search by topic. Ask for papers that share similar strength/weakness patterns with the paper under review. Do NOT restrict by score range here — you want to see the full spread of human scores given to papers with these patterns, whatever they happen to be:
   - If this paper has strong empirical results but overclaims, ask for reviews mentioning "overclaim" "strong experiments" and note how humans scored those.
   - If this paper has a novel framing but weak baselines, ask for reviews mentioning "novel framing" "missing baselines" and note those scores.

3. Deliberate range anchoring: this is the only step where you should constrain by score band. Use it to find papers on a similar topic (NOT similar strength/weaknesses) but at different quality levels, so you can see what high vs. low scoring looks like in your area. Retrieve multiple (ideally 2-4) papers per score range with topic as query, not just one — a single anchor is too noisy to rely on. When you ask `calibration_search` for a band, state the numeric score range explicitly (e.g. "avg human score between 4 and 6") rather than leaving it as "low-scoring" or "weak", so the subagent can apply the score filter. Use these exact bands:
   - High: avg human score >= 6. Request papers in this band and read a few to see what made them strong.
   - Medium: avg human score around 5. These are your borderline anchors.
   - Low: avg human score <= 4. Request papers in this band and read a few to see what made them weak. "Low" here means genuinely poor, not just below-average — a paper averaging 5 is medium, not low.
   - Compare the paper under review against all three bands. Every paper you review should be scored relative to at least one paper from each of the three bands, regardless of its topic. If nothing topically similar came back in the low band, still take whatever the subagent returned in the <=4 band as your low anchor rather than skipping the band.

   Examples: if reviewing a paper about privacy attacks on face recognition:
   - "Find papers on privacy attacks / face recognition with avg human score >= 6. Return 3-5 paths with one-sentence summaries of what made them strong."
   - "Find papers on privacy attacks / face recognition with avg human score <= 4. Return 3-5 paths with one-sentence summaries of what made them weak."
   - "Find face-recognition evaluation papers with avg human score >= 6."
   - "Find privacy-evaluation papers with avg human score <= 4."

   If no papers are found with the same topic, relax topic but keep the score band — it is better to have an off-topic low anchor than no low anchor at all.

4. Score relative to anchors: your final score should be positioned relative to the retrieved examples. If retrieved papers with similar strengths got 7s from humans, and papers with similar weaknesses got 3s, use that range. Do not compress everything into 4-6.

5. Score from the anchors, not from how the merged review reads. Papers with many listed weaknesses can still score high if their anchors did. Lean on the anchor range when your gut disagrees with it.

Retrieval is noisy — a single 8 or 3 doesn't pin your score. Use the center of the anchor cluster, weighted by topical similarity, and move outside that range only if the paper clearly beats or falls below most of the anchors.

Ordering matters: compare the paper to the retrieved anchors first, and let the comparison determine the score. Do not pick a score first and then go looking for anchors that support it — that defeats the point of calibration. If the anchors disagree with your initial intuition, move the score toward the anchors, not the other way around.

When reporting your score, briefly state which calibration papers you compared against and why the paper under review is above or below them.

You can use read_file to read the returned anchor files for more detail. List every anchor paper you retrieved, not only the ones that ended up shaping your final score — papers you looked at and decided did not fit are still part of the reasoning and must be shown. For each anchor give the path, its avg human score, and one sentence on how it compares to the paper under review. The list must include at least one low-scoring paper (avg score <=4), one medium-scoring paper, and one high-scoring paper (avg score >=6).

Let the score distribution follow the actual quality of the paper relative to the calibration examples.
The samples could be concentrated in the middle, that does not mean you have to score it in the middle as well.

There are less papers with extreme scores, so if the paper is truly exceptional or truly weak, it is okay to give it an extreme score even if most found papers are in the middle. You can also try to ask `calibration_search` for more papers with extreme scores to see what made a paper really good/bad.

Limit your `calibration_search` invocations to less than 20 rounds, do not dig too deep into retrieval.


