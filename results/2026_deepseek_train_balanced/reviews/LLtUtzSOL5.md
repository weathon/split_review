Now let me produce the final review. I need to be careful about calibration.

The fine-tuning gap is real and substantial. But I should not call it "fatal" because the paper's core contribution (the SORT benchmark, Book-SORT dataset, human evaluation, and in-context experiments) does not depend on the fine-tuning claim. The fine-tuning claim is a prominent finding but not the paper's raison d'être. It's a Major issue — the authors need to provide the missing evidence, and the paper's narrative might need revision if the evidence doesn't support the claim. But the benchmark itself remains valuable regardless.

Score: 5.5. This reflects a paper with genuine contributions that is currently incomplete in one significant respect. At ICLR standards, this would need author response to resolve before acceptance.

Decision: Reject (as currently submitted, the evidentiary gap in a headline claim prevents acceptance).

---

## Summary

This paper introduces SORT (Sequence Order Recall Tasks), a benchmark requiring LLMs to judge which of two text segments appeared first in a source document — a task adapted from recency-judgment paradigms used in cognitive psychology to study episodic memory. The authors contribute Book-SORT, a 36k-sample dataset from 9 recently public-domain books with controlled variation across excerpt length, segment length, and inter-segment distance; a human experiment with 155 participants providing a long-term memory baseline (64–76% accuracy); and evaluations of 11 models under in-context, fine-tuning, and RAG conditions. The main empirical finding is that models perform well (~95%) when the full excerpt is provided in-context but poorly when relying on parametric memory (fine-tuning) or vanilla RAG.

## Strengths

1. **Rigorous baseline validation that SORT requires book-specific memory.** Table 1 shows all 11 models scoring between 49% and 57% (near chance) when tested without access to the relevant books. This control is essential for establishing that SORT genuinely measures memory for specific text rather than general temporal or commonsense reasoning.

2. **Human experiment with high ecological validity.** Section 4.2 describes recruiting 155 actual Goodreads readers who had recently finished *The Murder of Roger Ackroyd*, testing them at an average of 7.5 days after reading (far beyond short-term memory duration), and demonstrating 64–76% accuracy. This provides a meaningful information-processing baseline that most benchmark papers lack.

3. **Careful multi-factor dataset design.** Section 4.1 systematically varies excerpt length (L_E ∈ {250,1000,2500,10000,20000} words), segment length (L_S ∈ {20,50} words), and inter-segment distance (D_S, binned), with 4 different segment pairs per distance bin to avoid content-distance confounds, counterbalanced correct answers, and sentence-boundary-aligned excerpts. This level of controlled variation supports the paper's nuanced findings about how each factor affects performance.

4. **Prompt selection methodology.** Section 3.1 describes compiling 12 prompt variants and selecting the best-performing prompt per model on a held-out set of 400 samples — methodologically more careful than typical single-prompt evaluations.

5. **Principled discussion connecting model behavior to cognitive theory.** Section 6 provides a coherent explanation for why in-context memory degrades with context length (arguing it is more analogous to working memory than episodic memory, which is sequence-length invariant) and why parametric memory as currently implemented cannot support episodic functions.

## Weaknesses

### Major

1. **The fine-tuning claim — featured prominently in the abstract and contributions — is reported without any supporting numerical evidence (Section 4.2).** The abstract asserts that "models fine-tuned with a language modeling objective on the book texts do not significantly improve their SORT performance, showing that parametric memory in current transformer models supports semantic but not episodic long-term memory." The contributions list claims models "fail to recall segment order based on parametric memory formed via fine-tuning." Yet Section 4.2 consists of exactly one sentence (line 226): *"For Llama3-8b-Instruct and Mistral-7b-v0.2-Instruct, we do not observe any difference in performance on SORT after memory is inserted via fine-tuning on large chunks of book-text."* There is no table, no figure, no accuracy numbers, no confidence intervals, no perplexity verification that the fine-tuning actually embedded book content in the model's parameters, and no information about training epochs or convergence. This is not a minor omission — it is a central claim of the paper rendered unverifiable as submitted. The paper's core benchmark contribution (SORT, Book-SORT, human evaluation, in-context results) remains valuable regardless of how the fine-tuning result turns out, but the reported narrative cannot be evaluated on this point until the evidence is provided.

### Minor

2. **Framing tension: the title and abstract push "assessing episodic memory," but the in-context condition tests positional reasoning from directly available text, not memory from prior encoding.** The strongest results (up to 95%) come from the condition where the model reads the excerpt and the two segments in the same forward pass — this evaluates whether the model can infer which segment came first in text it can directly attend to. Section 6 explicitly acknowledges that in-context memory is "more analogous to working memory" (line 260) and that its length-dependence is "inconsistent with human episodic memory" (line 258). The abstract and contributions should be scoped to match this careful discussion rather than presenting all conditions as "episodic memory" evaluation.

3. **Human experiment tested only one book and used a potentially biased recruitment pool.** All 155 participants read the same Christie novel, and recruitment via Goodreads self-selection (readers who opt into surveys after finishing a book) likely oversamples engaged readers with better recall. The paper does not discuss these limitations. This does not invalidate the human baseline but limits its generalizability.

4. **RAG results rely on qualitative ranges and figures rather than tabular precision.** The paper reports RAG accuracy as "between 55% and 67%" and provides figures rather than tables with confidence intervals. The oracle RAG condition does not report the proportion of samples for which both relevant passages were successfully retrieved (the denominator of that analysis), making it hard to assess how selective the oracle result is.

5. **No analysis of failure patterns.** The paper does not examine whether errors concentrate on semantically similar segments, segments with small distances, or other systematic patterns — analysis that would strengthen the benchmark's diagnostic value.

### Trivial

6. The fine-tuning description includes learning rate and batch size but omits training epochs or steps.

## Nice-to-Haves

- Perplexity verification that fine-tuning reduced loss on held-out book text (to confirm the model actually learned content, not just that SORT performance didn't change)
- Reporting the proportion of successfully retrieved samples in the oracle RAG condition
- Discussion of whether near-duplicate segment pairs exist in Book-SORT (the paper assumes 100% ceiling but does not verify)

## Removed Points

The following points from the inputs were filtered per the review guidelines:

- **Harsh critic's "structural/fatal" classification of the fine-tuning gap** → Downgraded to Major. The fine-tuning claim is a significant gap, but the paper's core contribution (the SORT benchmark framework, Book-SORT dataset, human evaluation, and in-context experiments) does not depend on this claim. The paper can be fixed by providing the missing data; the benchmark remains valuable regardless.
- **Harsh critic's claim about RAG comparison being "structurally uneven"** → The paper explicitly acknowledges the asymmetry at line 231 ("This difference in performance follows from the fact that standard forms of RAG do not necessarily preserve the order of retrieved passages"). This is adequately addressed by the authors; the remaining concern is downgraded to a presentation nitpick (point 4 above).
- **Harsh critic's request for equivalence testing on fine-tuning** → Subsumed by the larger gap: the paper reports no numbers at all, so statistical testing is moot until basic results are provided.
- **Strength Finder's generic/superficial phrasings** were removed, retaining only concrete, evidence-backed strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between the paper's ambitious framing ("assessing episodic memory") and what the in-context condition actually measures. This is a framing mismatch that the authors themselves partially resolve in the Discussion — they could clean it up by aligning the abstract and title with the more precise language used there.

## Suggestions

1. **Report the fine-tuning experiment fully.** Provide a table with pre- and post-fine-tuning SORT accuracy (with confidence intervals) for both Llama3-8b-Instruct and Mistral-7b-v0.2-Instruct, alongside perplexity on held-out book text to verify that the LM objective actually embedded book knowledge. Report training epochs, steps, and whether training converged. If the data supports the claim, this resolves the single largest gap. If it does not, revise the narrative accordingly — the benchmark is still a contribution.
2. **Reframe the abstract and title** to better match what the in-context condition evaluates: e.g., "evaluating temporal order recall in LLMs" rather than "assessing episodic memory." The Discussion already gets this right; the front matter should follow suit.
3. **Add tabular numerical results for the RAG condition** alongside the figures, and report the success rate of the oracle retrieval condition.
4. **Discuss the single-book and self-selection limitations** of the human experiment.
5. **Add a failure analysis**: do errors concentrate on semantically similar segments, segments with small distances, or particular books?

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>