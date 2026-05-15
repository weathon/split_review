Now I have all the information needed. Let me produce the final consolidated review.

## Summary

2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
// typically empty

### Major
- weakness 1 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

---

Here is my final review:

## Summary

This paper proposes Gramtector, a method for detecting AI-generated text by learning interpretable grammatical patterns (PoS n-grams) that discriminate human from machine writing. The key idea is to use L1-regularized logistic regression on a large set of PoS n-gram features, yielding ~20 sparse patterns that are both highly predictive (near-perfect AUROC on most domains) and human-comprehensible. A human trial shows that providing these patterns to non-expert labelers raises their detection accuracy from ~40% to ~86%.

## Strengths

1. **Novel and effective use of PoS n-grams for AI text detection.** The paper demonstrates that grammatical structure alone — without any semantic features — achieves AUROC scores close to 1.0 across arXiv, Wikipedia, Reddit, and CNN datasets, matching or exceeding RoBERTa/DistilBERT on several domains (Figure 2). This is a genuinely interesting finding that grammatical fingerprints of LLMs are highly discriminative.

2. **Interpretable by design, unlike black-box DNN detectors.** The method produces ~20 sparse PoS patterns with signed coefficients directly indicating whether each pattern is human-indicative or AI-indicative. This transparency is a concrete advantage over fine-tuned BERT-style classifiers and addresses a real concern about false accusations without explanation (Section 1, line 12).

3. **Generalization across LLMs and domains.** The method is evaluated on texts from ChatGPT, GPT-4, BARD, and LLAMA-2-70B across scientific abstracts, social media, news, and Wikipedia, achieving high AUROC on all model/domain combinations except BARD (where all methods struggle). This demonstrates the approach is not tailored to a single model or genre (Section 5.1).

4. **Human trial demonstrates transferable insights.** The human study shows that providing these grammatical patterns to non-expert labelers raises accuracy from ~40% (below chance) to 86% at the optimal guidance level (Level 1, PoS tagging). This directly demonstrates that the interpretability benefit of the method is realizable in practice (Section 5.2, Figure 4b).

## Weaknesses

### Major
None.

### Minor

1. **Missing DNN baselines in the robustness evaluation.** Table 2 compares Gramtector only against "vocabulary features" and "stylometric features" under adversarial attacks, not against the DNN-based detectors (RoBERTa, DistilBERT) used in Figure 2. While the paper's claim is about the relative robustness of grammatical vs. vocabulary/stylometric features — and the results support that — the absence of DNN baselines limits the strength of the general "robustness" claim. The paper would be stronger if it showed that grammatical features also resist paraphrasing better than, e.g., a fine-tuned RoBERTa detector under the same attacks. (Section 5.1, Table 2)

2. **Human trial lacks key details for reproducibility.** The paper does not report the number of participants, how many trials were run per condition, how abstracts were selected for the study, or the exact criteria for classifying responses as "unengaged" vs. "engaged" (Section 5.2). The engagement categorization is mentioned only as addressing "the trend of using LLMs to complete online surveys" with a reference to Veselovsky et al. (2023), but the operational definition is absent. These omissions prevent independent replication and raise questions about potential selection bias in the reported 86% figure (which is based on "engaged" participants).

3. **Inconsistency in reported baseline accuracy.** The abstract states the improvement is "from 43% to 86%" (line 4), while the introduction and conclusion both say "from 40% to 86%" (lines 19, 157). This is a careless reporting error that should be corrected.

4. **Human-in-the-loop framing is somewhat overclaimed relative to the evidence.** The automated logistic regression classifier already achieves near-perfect AUROC and is inherently interpretable (its coefficients directly indicate which patterns predict human vs. AI writing). The human trial shows that humans with pattern assistance reach 86% — strictly lower than the automated classifier. The paper would benefit from more clearly motivating *why* a human-in-the-loop is needed beyond interpretability (e.g., accountability, recourse in high-stakes settings), rather than framing it as the primary validation of the method.

5. **Justification for 20 patterns via Miller's law is weak.** The paper invokes Miller's law (capacity to retain ~9 items) to motivate sparsity, then selects 20 patterns — more than double the cited cognitive limit — and calls this a "trade-off." This reasoning, while not contradictory, is strained. A simpler justification (the L1 regularization path naturally selected ~20 useful features) would suffice and be more honest. (Section 4, line 65)

### Trivial
- The formalization of the highlighting function h_φ (Equation 2) is presented but never operationalized in the experiments; clarifying how it connects to the actual human-trial interface would help.
- The paper does not list the exact 20 learned PoS patterns or their coefficients (though these may appear in a figures/images not accessible in the text-only version).

## Nice-to-Haves
- Show the robustness results with DNN-based detectors (RoBERTa, etc.) included as baselines in Table 2.
- Provide the exact 20 learned patterns and their coefficients in a table to fully support the interpretability claim.
- Add a simple experiment comparing the human-in-the-loop approach against just showing participants the logistic regression coefficients (to isolate the value of highlighting).
- Include confidence intervals or error bars for the DNN baseline results in Figure 2, as is done for Gramtector.

## Removed Points

*These points are flagged for removal and should be treated with caution:*

- **"Baseline human accuracy of 40% is implausible and invalidates the reported improvement"** — REMOVED. Below-chance human performance on AI text detection is well-documented in the literature (Ippolito et al. 2020, Kobis et al. 2021). The paper acknowledges this ("worse than random guessing"). This does not invalidate the study; it is an expected finding. The 43%/40% inconsistency (kept above) is a separate, valid concern.
- **"The paper does not discuss how their domain-restricted setup avoids Sadasivan et al.'s impossibility results"** — REMOVED. The paper explicitly states: "As the problem of detection has been shown to be intractable in the most general setting... we focus on a case where there is an available dataset of human written text from a certain domain" (line 17). This is a direct acknowledgment.
- **"The human-in-the-loop approach is fundamentally unmotivated"** — REMOVED as stated. The paper motivates interpretability and the need to provide explanations to those falsely accused (line 12). Weakened version kept in Minor Weaknesses (#4).
- **"Engagement categorization introduces experimenter bias"** — REMOVED. This is speculative; there is no evidence of bias. The lack of definitional transparency is kept as a valid concern in Weakness #2.
- **"The paper does not discuss why BARD performance is poor"** — REMOVED. The paper discusses this: "It is possible that BARD-produced texts better resemble their human-written counterparts or that the model uses a more diverse language" (line 87).
- **"Strawman" and "formatting/style nitpicks"** — Various minor claims about missing appendix/proofs, formatting, etc. REMOVED per instructions.
- **Strength: "Principled feature selection guided by cognitive limits"** — DROPPED as it conflicts with the verified weakness about the Miller's law / 20 > 9 tension.
- **Strength: "Formal human-in-the-loop framework"** — DROPPED as the formalization (h_φ, Equation 2) is presented but never operationalized in the evaluation, making it a generic contribution.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: the strongest result (automated classifier with near-perfect AUROC) and the human-in-the-loop result (86% accuracy) are in some tension. The paper implicitly assumes that interpretability requires a human decision-maker, but the logistic regression on 20 sparse features is itself interpretable. This raises a deeper question: what does "interpretability" mean in an AI detection context — is it about understanding the model's decision rule, or about giving humans the final say? The paper's results at Guidance Level 1 (PoS tagging) outperform Level 3 (classified patterns), suggesting that requiring humans to actively engage with the features yields better outcomes than passive consumption of model outputs — a finding that resonates with work on appropriate reliance in human-AI decision-making but that the paper does not fully unpack.

## Suggestions

1. **Clarify the motivation for human-in-the-loop.** State explicitly whether the goal is accuracy (in which case the automated classifier wins), transparency/accountability (in which case human involvement is justified even at a slight accuracy cost), or something else. This reframing would make the contribution much clearer.

2. **Report the number of participants and the engagement classification criteria.** Without these, the human trial results cannot be independently assessed. At minimum, state N, how categories were assigned, and whether results change when unengaged participants are included.

3. **Add DNN baselines to the robustness table.** Even if they are too expensive to run on all conditions, a representative subset (e.g., RoBERTa on the paraphrased set) would significantly strengthen the robustness claims.

4. **Correct the 43%/40% inconsistency** and ensure numbers are consistent throughout.

5. **List the 20 learned patterns** (either in the main text or a clearly referenced appendix/table) to fully substantiate the interpretability claim.

## Score and Decision

This paper presents a genuinely novel and interesting approach to AI text detection using PoS grammatical patterns. The automated detection results are strong, the method is inherently interpretable, and the human trial — despite some transparency issues — provides evidence that these patterns can be effectively communicated to non-experts. The main weaknesses (missing DNN baselines in robustness, insufficient human trial details, and a minor numerical inconsistency) are addressable and do not undermine the core contribution. The paper makes a solid empirical contribution with practical value.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>