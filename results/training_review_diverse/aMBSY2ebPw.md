Now I have a thorough understanding of the paper and can verify the reviewer claims against it. Let me produce the final consolidated review.

## Summary

This paper challenges the claim from Tanzer et al. (2024) that long-context LLMs can effectively exploit a grammar book's grammatical explanations for extremely low-resource (XLR) translation. Through a clean ablation of grammar-book components (parallel sentences vs. grammatical explanations) for English↔Kalamang and English↔Nepali, the authors show that nearly all translation performance comes from parallel examples, not explanations. They further demonstrate that fine-tuning a small NLLB-1.3B model on the same parallel data matches or beats Gemini prompted with the full grammar book, and that a novel typological feature prompt achieves leading results on grammar-relevant linguistic tasks (IGT prediction, grammaticality judgment). The paper argues for task-appropriate data collection: parallel data for MT, grammatical/typological data for linguistic tasks.

## Strengths

1. **Clean ablation disentangling parallel examples from grammatical explanations** — The paper performs the crucial decomposition that prior work (MTOB) omitted. Table 1 shows that removing parallel data (Book$_{\neg p}$) drops quality by 7–8 ChrF++ vs. Book$_p$, while adding explanations atop parallel data (Book$_{all}$ vs. Book$_p$) yields only +3 ChrF++ into kgv and −0.3 into eng. This is the paper's strongest and most concrete finding.

2. **Generalization to a seen low-resource language** — The Nepali results (Table 2, Flores test set with 1012 examples) show the same pattern: Book$_{all}$ and Book$_{\neg p}$ either match or underperform Book$_p$. This strengthens the claim beyond the single unseen Kalamang case, using a larger and more standard evaluation set.

3. **Fine-tuned small MT models match long-context LLMs** — Table 3 shows that fine-tuning NLLB-1.3B on the same parallel data achieves 34.2 ChrF++ into kgv (vs. Gemini's 26.6 with P$_{book}$) and 38.7 with additional P$_{train}$ (vs. Gemini's 33.4). This is a practically important result: it shows the MTOB benchmark can be solved cheaply without costly long-context LLMs.

4. **Typological prompting achieves leading results on linguistic tasks** — The novel typological feature prompt (Typ+Book$_p$) achieves the best morpheme accuracy (46.1%) on IGT prediction (Table 4) and performs best on grammaticality judgment (Figure 1). This demonstrates that LLMs *can* exploit grammatical knowledge when given the right form and task, providing a nuanced counterpoint to the negative translation results.

5. **Token-efficiency analysis with practical implications** — The paper quantifies that the full grammar book uses ~5× more tokens than parallel-only prompts with no significant performance gain, making a concrete case for cheaper parallel data collection over linguistic description for MT purposes.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by the central ablation experiments. The weaknesses below are substantive but do not threaten the main conclusions.

### Minor

1. **Underpowered regression analysis for the "no significant advantage" claim** — The type-coverage regression (Section 5.2, Figure 2) relies on approximately 10–15 data points per direction. The key comparison (Book$_{all}$ vs. Book$_p$) involves points with nearly identical type coverage, so even a modest effect from explanations could be masked. The paper correctly uses hedged language ("no *significant* advantage"), but the statistical evidence for this claim is suggestive rather than conclusive. A control condition that adds non-grammar text with matched type coverage would substantially strengthen the negative claim. *(Note: the reviewer's claim that "the paper does not control for total parallel tokens" is incorrect — the paper runs a separate token-count regression finding no significant relationship. The issue is limited statistical power, not absence of control.)*

2. **Small Kalamang test set limits generalizability** — The Kalamang test set is 100 sentences (combined from MTOB's 50+50). The paper acknowledges this limitation (Section 2) but still draws conclusions about "LLMs failing to exploit grammar for translation" that would ideally be supported by larger held-out data. The Nepali results help, but Nepali is a seen language where 0-shot performance is already strong, making the comparison qualitatively different. This is an inherent limitation of the domain rather than an oversight, and the paper is reasonably cautious.

3. **Grammaticality judgment task has limited diagnostic value** — The paper acknowledges it cannot guarantee corruptions are ungrammatical (Section 3.4). The concern runs deeper: swap-adjacent corruptions in particular could produce plausible alternative word orders in a language without known syntactic constraints. All settings score near 50% accuracy (Figure 1), making it difficult to attribute differences to genuine grammatical understanding. This task does not provide strong evidence by itself; however, the paper's claims about LLMs exploiting grammar for linguistic tasks are better supported by the IGT results (Table 4), which are cleaner and more substantive.

4. **No confidence intervals or statistical significance tests on main translation comparisons** — The key comparisons in Table 1 (Book$_{all}$ vs. Book$_p$, Book$_p$ vs. Book$_{\neg p}$) are reported without bootstrapped confidence intervals or significance tests. Given the small test set (100 examples), readers cannot assess whether observed differences (e.g., +3 ChrF++ for Book$_{all}$ vs. Book$_p$ into kgv) are reliable.

5. **Supervised IGT baselines are trained on very small data** — The supervised IGT baselines use only 1221 training sentences (split 90:10). While the paper uses the best available methods from the SIGMORPHON shared tasks, the claim that "typological prompting achieves leading performance" should be contextualized as leading among methods trained/evaluated on this small Kalamang-specific dataset.

6. **Typological prompt construction details are sparse** — The paper does not specify how many typological features per language, which features were selected, or how the "short explanation" was generated (Section 3.3). A table or example prompt would aid reproducibility.

7. **No error analysis** — The paper would benefit from qualitative examples contrasting model outputs with Book$_{\neg p}$ vs. Book$_p$, to illustrate whether errors are lexical (OOV) or grammatical in nature.

### Trivial
None.

## Nice-to-Haves

- A control condition adding non-grammar text (e.g., random Wikipedia paragraphs) with matched type coverage on top of Book$_p$ would substantially strengthen the negative claim about explanations.
- Bootstrapped confidence intervals for the key translation comparisons in Table 1.
- An ablation of the typological prompt components (which features matter, is the "short explanation" necessary).
- A small error analysis with qualitative examples.

## Removed Points

These points from the reviews are flagged for removal; treat them with caution:

- **"The paper does not control for total parallel tokens"** (Harsh Critic, Critical Issue 1) — The paper explicitly runs a regression on total prompt tokens (Section 5.2, line 289) and finds no significant relationship (p=0.997, p=0.78). The reviewer's claim is factually incorrect; the real concern is limited statistical power, not absence of control.
- **Strength Finder Strength 4's phrasing that regression "proves" explanations provide no advantage** — The word "proves" overstates the evidence; the paper itself uses "no *significant* advantage," which is appropriately hedged. The strength as stated is too strong for the data, but the underlying finding (regression is significant, no point falls outside CI) is valid as a supporting observation.
- **Any criticism about grammar book splits not yet being released** — The paper states they will be made available after review, which is standard for the review process.
- **Any formatting/style nitpicks** — Parser artifacts, not author errors.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel synthesis: the paper provides evidence for a *task-dependent dissociation* in how LLMs use linguistic information — parallel data is sufficient for MT, but typological features help for linguistic tasks — which suggests that the form and granularity of grammatical knowledge must match the cognitive demands of the task. This is more nuanced than either "grammar helps" or "grammar doesn't help" and points toward a design principle for XLR resource use.

## Suggestions

1. Add a control condition with non-grammar text matched for type coverage on top of Book$_p$ to strengthen the negative claim.
2. Report bootstrapped 95% confidence intervals for the ChrF++ scores in Table 1, especially for Book$_{all}$ vs. Book$_p$ and Book$_p$ vs. Book$_{\neg p}$.
3. Include an example of the typological feature prompt in the appendix (or main text if space permits).
4. Add a brief qualitative error analysis contrasting Book$_{\neg p}$ vs. Book$_p$ translations for Kalamang.
5. Temper the grammaticality judgment framing as exploratory given the validity concerns.

## Score and Decision

This is a well-executed empirical re-evaluation paper with clear contributions: it directly refutes a central claim in prior work (MTOB) through careful ablation, demonstrates a practical cheaper alternative (fine-tuned NLLB), and provides a new method (typological prompting) that works on linguistic tasks. The weaknesses are real but modest in severity — the small test set is inherent to the domain and acknowledged, the regression is suggestive rather than conclusive but the main ablation evidence (Table 1) is independently convincing, and the grammaticality judgment task is secondary to the stronger IGT results. The paper is well-written, the experiments are sound, and the conclusions are appropriately hedged. The contribution is significant for XLR NLP practitioners making data-collection decisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>