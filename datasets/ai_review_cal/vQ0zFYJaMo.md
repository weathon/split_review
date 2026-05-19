- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5
Now I have a thorough understanding of the paper and both reviews. Let me construct the consolidated review, carefully verifying each claim against the paper text.

**Verifying key claims from the Harsh Critic:**

1. **Confound claim (similarity vs. diversity):** The paper's Section 4.2 (line 121) explicitly states: "Low-Similarity Dataset is more Diverse than High-Similarity one" and Figure 4 confirms this. The paper frames diversity as the mechanism, not a confound. But the title and Section 3 title ("FINE-TUNING TASK SIMILARITY TO ALIGNMENT DATA DEFINES THE DAMAGE") emphasize similarity as the causal factor. The paper does not attempt to disentangle the two. This is a valid criticism about framing, but the paper does acknowledge the correlation.

2. **Privacy overclaim:** Abstract says "importance of dataset diversity and privacy." Discussion (Section 5) discusses privacy extensively. But privacy is never experimentally tested. This is a valid criticism.

3. **Evaluation circularity claim:** The HC says "you measure safety using that task's own harmful examples." But the paper says (line 109): "We employed the HEx-PHI safety benchmark" — this is a separate general benchmark. The harmful downstream tasks (List Examples, Pure Bad) are used for *fine-tuning*, and safety is evaluated on HEx-PHI. The circularity criticism is incorrect.

4. **"Merely a consequence"** — line 21: "We argue that such harmful subsets in a benign dataset are merely a consequence of lacking alignment diversity." This is indeed an overstatement.

5. **Missing training details** — these would be in the appendix (stripped by parser). Remove per rules.

Let me write the review now.

---

**Strength Finder checks:**
- Strength 1 about "causal evidence" — the paper shows controlled comparisons but the confound weakens the causal claim. I'll keep this but caveat it.
- Strength 2 about anchor-free clustering — legitimate, supported by Section 3.1.
- Strength 3 about diversity metric — legitimate, supported by Section 3.2.
- Strength 4 about transparent pipeline — legitimate, supported by Section 4.1.

None of the strengths are generic/delusional/sycophantic. All are specific and evidence-based. I'll keep them all.

Wait, I should double-check - the HC says the anchor-free clustering experiment is "too brief" and has unclear baseline. Let me verify from the paper (lines 30-32):

"In the Alpaca dataset... We then select a cluster of list-format questions and randomly sample 100 data from them for fine-tuning. The results, shown in Table 1, indicate that high representation similarity within downstream datasets is more detrimental to safety guardrails than similarity to explicitly harmful data anchors (Top-100 Harmful). Notably, the high-similarity list group could increase the GPT Attack Success Rate (ASR) by 15%."

The baseline is Top-100 Harmful from He et al. (2024). This is clear from context. The HC's concern about unclear baseline is resolved by reading the text carefully. I'll remove this specific criticism.

Now let me produce the final review.Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper studies why fine-tuning degrades the safety guardrails of instruction-tuned LLMs. The central claim is that the similarity between upstream alignment data and downstream fine-tuning data determines guardrail durability — higher similarity leads to more fragile guardrails. The authors construct their own alignment pipeline (LLAMA2-7B-BASE + UltraChat + BeaverTails subsets), select alignment subsets that are either highly similar or dissimilar to a given downstream task using cosine similarity of representations, and measure safety degradation after fine-tuning across four downstream tasks (two harmful, two benign). They also find that low-similarity alignment subsets are more diverse than high-similarity ones, and that diversity correlates with guardrail durability.

## Strengths

1. **Controlled experimental comparison across four downstream tasks.** Table 2 shows that models aligned with the Low-Sim subset of BeaverTails consistently maintain lower harmfulness (GPT ASR) after fine-tuning compared to High-Sim and Random subsets across both harmful and benign tasks (List Examples, Pure Bad, Alpaca, SAMSum), while utility (MT-Bench / ROUGE-1) remains comparable. This is the paper's strongest empirical contribution — a practical demonstration that selecting alignment data dissimilar to anticipated downstream tasks produces more robust guardrails.

2. **Anchor-free clustering method for identifying harmful fine-tuning data (Section 3.1).** By applying k-means to the Alpaca dataset and fine-tuning on a high-intra-similarity list-format cluster, the paper shows a 15% higher GPT ASR than fine-tuning on He et al.'s Top-100 Harmful subset. This provides a principled way to identify harmful data without relying on explicit harmful anchors, and supports the idea that high homogeneity (low diversity) in fine-tuning data exacerbates safety degradation.

3. **Formal diversity metric linking similarity and guardrail durability.** The paper adapts a determinant-based diversity measure (Eq. 5) and shows in Figure 4 that Low-Sim alignment subsets consistently have higher diversity scores than High-Sim subsets across all four downstream tasks at both 1K and 5K subset sizes. This provides a quantitative property that correlates with safety outcomes.

4. **Transparent, from-scratch experimental pipeline (Section 4.1).** Instead of relying on proprietary alignment steps, the authors start from LLAMA2-7B-BASE, build instruction-following capability via UltraChat, and control the safety alignment data (BeaverTails subsets). This design allows direct, reproducible manipulation of upstream data composition.

## Weaknesses

### Fatal

None.

### Major

1. **The similarity–diversity confound is not disentangled, so the paper's strong causal claims about similarity *per se* are unsupported.** The selection procedure (Eq. 1) picks alignment data based on cosine similarity to downstream tasks. Naturally, the Low-Sim subset samples from a broad region of representation space (hence more diverse), while the High-Sim subset concentrates around the downstream task (hence less diverse). The paper itself shows this correlation in Figure 4 (line 121: "the low similarity subset consistently exhibits the highest diversity scores"). Consequently, the observed difference in guardrail durability could be driven by the diversity of the alignment data, not by the similarity relation *to the downstream task*. The paper conflates these two variables and never attempts to control for one while varying the other. The title ("Your Task May Vary") and Section 3 title ("Fine-tuning Task Similarity to Alignment Data Defines the Damage") emphasize similarity as the causal factor, but the evidence is equally consistent with "more diverse alignment data produces more robust guardrails" — a weaker claim. The paper would be strengthened by either (a) an experiment that varies similarity while controlling for diversity, or (b) a reframing that accurately describes what was demonstrated (diverse alignment subsets — which can be approximated by selecting data dissimilar to downstream tasks — produce more durable guardrails).

2. **Privacy is presented as a key finding but is never experimentally tested.** The abstract states the paper demonstrates "the importance of dataset diversity and privacy" and advocates a "dual strategy" prioritizing both. The Discussion (Section 5) extensively discusses privacy, transparency, and their trade-offs. However, no experiment in the paper tests privacy — no data leakage scenario, no adversarial access experiment, no differential privacy analysis. Privacy is discussed only as a speculative policy implication. Including it as a co-equal finding in the abstract and conclusion misrepresents what the paper actually studied.

3. **Unsupported strong claim in the introduction.** Line 21: "We argue that such harmful subsets in a benign dataset are merely a consequence of lacking alignment diversity." The word "merely" implies that lack of diversity is the sole cause. The experiments show an association but do not establish exclusivity. This overclaim weakens the paper's rhetorical credibility.

### Minor

1. **Construct validity of the safety alignment pipeline.** The paper constructs its own alignment by fine-tuning LLAMA2-7B-BASE on UltraChat + BeaverTails subsets, which is not equivalent to the multi-stage RLHF alignment used in production models like LLAMA2-CHAT. The paper acknowledges this briefly in Limitations (Section 5). However, the entire motivation (Figure 1) concerns the fragility of *existing* safety guardrails, so the applicability of findings to real-world aligned models is unclear. The paper partially mitigates this by testing on GEMMA2-2B/GEMMA2-9B (noted in Limitations), but doesn't directly test on a production-aligned model.

2. **No confidence intervals or variance reported.** The paper reports only mean values for GPT ASR and GPT Score across conditions. Especially given the small fine-tuning dataset sizes (100 examples for harmful tasks), variance estimates, standard deviations, or per-seed results would significantly strengthen reliability assessment.

3. **Reliance solely on GPT-3.5-based evaluation.** Safety is evaluated entirely through GPT-3.5 scoring (GPT Score, GPT ASR). While common practice, LLM-based evaluators have known biases (e.g., preference for longer responses, sensitivity to formatting). Supplementary automated safety benchmarks or human evaluation would strengthen the results.

### Trivial

None.

## Nice-to-Haves

- Testing on a held-out set of harmful prompts completely unrelated to the downstream tasks used for alignment subset selection would help establish generalizability.
- Explicitly stating whether the "uncensored chat model" ℳ used for representation extraction is the model fine-tuned on UltraChat without BeaverTails (implied but not stated in Section 3.2).
- Clarifying why Alpaca "List Examples" are categorized as a harmful task when the full Alpaca dataset is categorized as benign — the paper could explain that the list-format cluster is *treated as harmful* only because fine-tuning on it causes jailbreaks, not because of content.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Correlation vs. causation (HC Point 2):** The HC claims only correlation is shown. In fact, the paper *intervenes* by selecting specific alignment subsets (High-Sim vs. Low-Sim vs. Random) and measuring downstream safety. This is an experimental manipulation, not passive correlation. Removed because it mischaracterizes the paper's design.
- **Evaluation circularity (HC Section 4.2 note):** The HC claims "you fine-tune on a task, and you measure safety using that task's own harmful examples." The paper states (line 109) that it uses the **HEx-PHI safety benchmark** — a separate, general-purpose safety evaluation. Safety is not evaluated on the fine-tuning data itself. Removed as factually incorrect.
- **Unclear baseline for Table 1:** The HC says it's "unclear" what the 15% increase is compared against. The paper clearly states (line 32) the comparison is against He et al.'s Top-100 Harmful subset. Removed as a misreading.
- **Missing fine-tuning hyperparameters:** The HC requests training epochs, learning rate, optimizer. These are standard implementation details likely in the appendix (stripped by PDF parser). Removed per rule about parser-stripped content.
- **Missing related work:** Per instruction, I cannot comment on missing citations as I lack external verification.
- **Formatting/style nitpicks:** None from either reviewer.
- **"Strengthening the Paper on Its Own Terms" section:** Moved to suggestions/nice-to-haves rather than weaknesses.
- **Generic strength (Strength Finder bullet about "transparent pipeline"):** This is specific enough (it describes a concrete design choice). Kept.
- **Strength Finder's "causal evidence" framing:** The strength itself is about the controlled comparison, which is valid. The word "causal" is softened by the confound weakness above; the data is still valuable.

## Novel Insights

A genuinely novel observation that emerges from synthesizing the two reviews is that the paper's main empirical finding (Low-Sim > High-Sim) is robust and practically useful *regardless of whether the mechanism is similarity or diversity*. The practical recommendation — "select alignment data that is dissimilar to your anticipated downstream tasks" — is a concrete, actionable guideline that model deployers can implement with any off-the-shelf embedding model. The controversy over mechanism (similarity vs. diversity) is scientifically important but does not diminish the practical utility of the result. This is worth highlighting because it means the paper's experiments are not wasted even if the causal interpretation needs refinement.

## Suggestions

1. **Reframe the contribution.** Adjust the title, abstract, and discussion to accurately describe what was shown: that alignment data selected to be dissimilar to downstream tasks produces more durable guardrails, and that this correlates with increased diversity of the alignment subset. Remove or soften claims about privacy being an experimentally supported finding.
2. **Address the similarity–diversity confound directly.** If the paper aims to claim similarity *per se* is causal, design an experiment that varies similarity while holding diversity constant (e.g., create two alignment subsets matched on diversity score but differing in cosine similarity to the downstream task). If such separation is infeasible, explicitly acknowledge that the observed effect may be driven by diversity, and reframe the contribution accordingly.
3. **Add variance estimates** (confidence intervals, standard deviations, or per-seed results) for all reported metrics.
4. **Remove or heavily qualify the "merely a consequence" claim** (line 21), as the experiments do not establish exclusivity.
5. **Consider adding a held-out safety evaluation** using prompts from a completely different domain than the downstream tasks used for subset selection, to strengthen generalizability.
