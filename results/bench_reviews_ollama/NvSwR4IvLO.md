Now I have a thorough understanding of the paper. Let me compile my analysis of each harsh critic point:

**Point 1: Recursive paraphrasing not applied to neural network-based and zero-shot detectors.**

This is partially valid. The abstract says "we develop a recursive paraphrasing attack to apply on AI text, which can break a whole range of detectors, including the ones using the watermarking schemes as well as neural network-based detectors, zero-shot classifiers, and retrieval-based detectors." However:
- For watermarking: recursive paraphrasing (DIPPER/LLaMA-2) applied ✓
- For retrieval-based: recursive paraphrasing (DIPPER) applied ✓
- For zero-shot (DetectGPT): single-round T5 paraphrasing applied, not recursive paraphrasing with DIPPER
- For neural network-based (RoBERTa): single-round T5 paraphrasing applied, not recursive paraphrasing with DIPPER

The 96.5% → 25.2% DetectGPT figure from the introduction is actually unclear — the actual body text says 96.5% → 59.8% after T5 attack. Let me check what the 25.2% refers to... It must come from the multi-query (10 queries) setting with T5. The abstract mentions "recursive paraphrasing" breaking all four classes, but for two of the four, a different and weaker attack (single-round T5 / multi-query T5) was used. The conclusion actually softens this claim somewhat: "we develop a strong attack called recursive paraphrasing that can break recently proposed watermarking and retrieval-based detectors."

This is a valid criticism — the paper's abstract and introduction conflate two different attacks (recursive paraphrasing vs. single-round/multi-query T5) under the "recursive paraphrasing" banner. However, the distinction is nuanced: the paper's broader point is that paraphrasing attacks break detectors, and recursive paraphrasing is the strongest variant tested against watermarking and retrieval. The framing in the abstract is misleading but the results still show vulnerabilities across all four classes. I'll classify this as a **major** weakness — it's a real overclaim in the framing, but not fatal because the actual experimental results do show non-trivial degradation across all classes.

**Point 2: Paraphraser-to-target model size asymmetry.**

Valid observation but the severity is overstated. The paper uses T5 (222M) against GPT-2 Medium (355M), which shows the attack works even with a smaller paraphraser in that case. For watermarking experiments, DIPPER (11B) vs OPT-1.3B or (13B) is comparable or the target is slightly larger. The argument that this limits generalizability is reasonable but somewhat speculative. I'll classify as **minor** — the size asymmetry does affect the strength of conclusions about "practical scenarios," but the paper does demonstrate one case where a smaller paraphraser works (T5 vs GPT-2 Medium).

**Point 3: Theoretical hardness claim overreaches.**

This is mostly valid but the paper itself acknowledges limitations. The paper says "Although not a surprising result" (line 37) and acknowledges the difficulty of estimating TV. The meta-token projection to 5 partitions is indeed a very coarse approximation. However, Theorem 1 is a provably correct upper bound — the claim that AUROC decreases as TV decreases is mathematically correct. The overreach is in how compellingly the paper argues that TV → 0 in practice for modern LLMs. I'll classify as **major** — the empirical evidence for the key assumption (TV decreasing with model capability) is too weak to support the strong existential claims.

**Point 4: Human evaluation measures wrong quantity.**

This is a valid point. The MTurk studies measure content preservation and grammar quality, not whether paraphrased text is indistinguishable from human text. However, the paper's claim is slightly more nuanced — it claims quality is "slightly degraded" and detectors are broken, not directly that paraphrased text is "indistinguishable from human text." Still, to claim the attack is practical, one would want to know the paraphrased text actually passes as human. I'll classify this as **minor** — it's a gap that weakens but doesn't invalidate the findings, since the detector performance metrics themselves show evasion.

Now let me assess the Strength Finder's claims:

- Strength 1 (recursive paraphrasing effective against watermarking): Valid and well-documented.
- Strength 2 (broad coverage across four detector classes): Partially valid — broad coverage exists but the attack type differs across classes, so this is weaker than claimed.
- Strength 3 (theoretical hardness result): Valid but limited by the weakness in empirical support noted above.
- Strength 4 (spoofing attacks without white-box access): Valid.
- Supporting Strength 1 (multi-faceted quality preservation): Valid but limited as noted in weakness.
- Supporting Strength 2 (empirical support for TV assumption): This is actually a weakness, not a strength — the evidence is too weak.
- Supporting Strength 3 (long passages): Valid.
- Supporting Strength 4 (retrieval-based spoofing): Valid.

Let me now write the final review.</think>Now I have a thorough understanding of the paper. Let me compile my final review.

## Summary

This paper investigates the reliability of AI-generated text detectors by developing a "recursive paraphrasing" attack that repeatedly paraphrases LLM outputs using powerful paraphrasers (DIPPER, LLaMA-2-7B-Chat). The attack is shown to dramatically degrade watermarking and retrieval-based detectors. The paper also demonstrates spoofing attacks that increase false positive rates, and provides a theoretical result (Theorem 1) linking the AUROC upper bound of any detector to the total variation (TV) distance between human and AI text distributions.

## Strengths

- **Recursive paraphrasing is strikingly effective against watermarking detectors**: TPR@1%FPR for soft watermarking on OPT-13B drops from 99.3% to 9.7% after 5 rounds of DIPPER paraphrasing, and to 4.0% with "best of ppi" selection, with only a 2.2 increase in perplexity (Figures 2–3). This substantially surpasses the weaker span-replacement attack considered in the original watermarking paper (Kirchenbauer et al.), making it a genuine contribution.

- **Retrieval-based detector vulnerability to recursive paraphrasing is a non-obvious result**: The detector from Krishna et al. was explicitly designed to resist paraphrasing attacks, yet its accuracy falls from 100% to below 60% after 5 rounds of DIPPER paraphrasing with only a 1.7 perplexity increase (Figure 5). This is an important finding since it undermines a detector specifically claimed to be paraphrase-robust.

- **Proof-of-concept spoofing of watermarking schemes without white-box access**: By querying a watermarked OPT-1.3B one million times, an adversary can estimate green lists for 181 common words and collapse watermarking AUROC from 99.8% to 1.3% (Section 3, Figure 6). This is a practically relevant attack not previously demonstrated.

- **Paraphrasing attacks degrade zero-shot detectors significantly**: DetectGPT AUROC drops from 96.5% to 59.8% after single-round T5 paraphrasing (Figure 4 middle), showing these detectors are fragile even to relatively weak paraphrasing.

## Weaknesses

### Fatal
None.

### Major

- **The abstract and introduction conflate two different attacks under the "recursive paraphrasing" banner, misattributing results to the headline method for half the claimed detector classes.** The paper's central claim is that "recursive paraphrasing" breaks watermarking-based, neural network-based, zero-shot, and retrieval-based detectors (Abstract, line 4). However, recursive paraphrasing (using DIPPER/LLaMA-2 with multiple rounds) is only applied to watermarking (§2.3) and retrieval-based (§2.4) detectors. For neural network-based and zero-shot detectors (§2.4), a fundamentally different and weaker attack is used: single-round T5-based paraphrasing (222M parameter model, sentence-by-sentence). The most dramatic number cited for DetectGPT in the introduction—AUROC dropping from 96.5% to 25.2%—comes from yet another setup (multi-query with ten T5 paraphrases), not recursive paraphrasing. Even the conclusion (line 337) correctly narrows the claim to "recursive paraphrasing that can break recently proposed watermarking and retrieval-based detectors," but the abstract and introduction do not make this distinction. This mismatch between the headline contribution and the experimental evidence for two of the four detector classes undermines the paper's framing as a comprehensive analysis showing that one method breaks all detectors.

- **The theoretical hardness result's empirical support is too weak to sustain the paper's strong existential claims about detection impossibility.** Theorem 1 correctly establishes that AUROC(D) ≤ ½ + TV(M,H) − TV(M,H)²/2, meaning detection becomes harder as TV decreases. However, the empirical evidence that "TV decreases with model capability" in realistic settings is strikingly weak: (i) single-layer LSTMs learning Markov chains on length-3 sequences (Figure 7), and (ii) a "meta-token" projection collapsing the entire vocabulary into 5 partitions before estimating TV (Figure 8). Neither remotely resembles the scale or structure of modern LLM text distributions. The paper acknowledges ("estimating the exact TV between text distributions from a finite set of samples is a challenging problem," line 318) but does not discuss how the projection approximation error might affect the TV estimates or whether TV in the projected space reflects TV in the original token space. Additionally, the paper's specific claim that "TPR > 0.9 at FPR < 0.01 cannot be achieved even when the overlap between the distributions is relatively low, say 11%" (TV = 0.89) is misleading: the bound gives AUROC ≤ 0.994 at TV = 0.89, which is fully compatible with that level of performance—the upper bound provides no basis for claiming infeasibility at that TV value. The theorem is a valid upper bound, but the paper overstates its practical implications.

### Minor

- **The paraphraser-to-target model size asymmetry limits the generalizability of claims about "practical scenarios."** For watermarking experiments, DIPPER (11B) paraphrases outputs of OPT-1.3B or is comparable to OPT-13B; the paraphraser is at least as capable as the target. For the non-watermarking experiments, the weaker T5 (222M) is used against GPT-2 Medium (355M), showing the attack works with a somewhat smaller paraphraser—but this is the one case and the results are less dramatic (RoBERTa retains 92% TPR@1%FPR after single-round T5 paraphrasing). The paper does not discuss the implicit assumption that an effective recursive paraphraser must be comparable in capability to the target LLM, nor how this affects conclusions for attacks against frontier models. This isn't fatal to the findings—the results for available model pairs are valid—but it limits how strongly one can extrapolate to "practical scenarios" involving much larger target models.

- **The human evaluation measures content preservation and grammar, not the property most relevant to the claims: whether paraphrased text is indistinguishable from human text.** The MTurk studies (Tables 1–2) rate content preservation (70% high quality) and grammar (89% high quality), which addresses whether the attack degrades text usability. However, the core evasion claim requires that paraphrased text pass as human, and showing good grammar/content preservation ≠ showing human-likeness. A direct human-vs-AI classification task by annotators would more directly validate the attack's evasion effectiveness. That said, the detector performance metrics themselves (e.g., TPR dropping to 9.7%) provide strong evidence of evasion independently of the human evaluation, so this gap weakens the quality story but not the core detection results.

### Trivial
None.

## Nice-to-Haves

- Testing recursive paraphrasing (DIPPER/LLaMA-2) directly on neural network-based and zero-shot detectors would unify the experimental methodology across all four detector classes and eliminate the framing mismatch.
- A tighter empirical validation of the TV-distance assumption, e.g., using better TV estimators or evaluating on more realistic LLM settings, would significantly strengthen the theoretical contribution.
- Human evaluation where annotators classify paraphrased AI text vs. human text would directly validate the evasion claim.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Not a surprising result" dismissal of Theorem 1** (from Strength Finder's Supporting Strength 2): The Strength Finder claims empirical support for the TV assumption as a strength, but the empirical evidence is actually the paper's weakest point—the synthetic LSTM experiments and 5-partition meta-token projections are too far removed from real LLM distributions. This conflicts with the verified weakness above, so it is removed.

- **"Broad empirical coverage across all four detector classes with consistent vulnerability findings" as a strength** (Strength Finder's Strength 2): This conflicts with the verified major weakness that recursive paraphrasing was not actually applied to two of the four classes. The coverage exists but the attack paradigm differs across classes, making "consistency" misleading.

- **"70% high quality" content preservation being downplayed** (Harsh Critic's Point 4 sub-point): While 30% non-high-quality is noted, the paper does report this number explicitly with both 70% and 23% "somewhat equivalent," so it is not truly downplayed—it is transparently reported. The more substantive issue is what the metric measures, which is captured in the minor weakness above.

- **Watermark spoofing limited to 181 common words** (Harsh Critic §3): This is a proof-of-concept demonstration, which the paper explicitly frames as such. Limiting to 181 words is a practical design choice for the proof-of-concept and doesn't invalidate the finding that the watermarking scheme's green lists can be extracted.

- **Zero-shot spoofing via prepending text is "naïve"** (Harsh Critic §3): The paper itself acknowledges this is naïve (line 269: "naïve spoofing attack"). Criticizing a proof-of-concept for being simple when the paper already acknowledges its limitations is not substantive.

- **Demanding experiments with GPT-3.5/GPT-4** (Harsh Critic Missing Experiments #5): The paper studies open-source models where controlled experiments are feasible. This is a scope limitation, not a methodological flaw. Nice-to-have only.

## Novel Insights

The most important observation that emerges from careful reading is that the paper unknowingly demonstrates a gradient of detector vulnerability that it does not fully acknowledge: zero-shot detectors (DetectGPT AUROC → 59.8% after single T5 round), retrieval-based detectors (accuracy → ~60% after recursive DIPPER), watermarking detectors (TPR@1%FPR → 9.7% after recursive DIPPER), and trained neural network detectors (RoBERTa retains 80% TPR@1%FPR even under optimal multi-query attack). This gradient—from most vulnerable (zero-shot), to medium (watermarking/retrieval under recursive attack), to relatively robust (trained classifiers)—suggests the paper's uniform pessimism about "all detectors" is not fully supported by its own data. Trained detectors show meaningful resilience, and the paper's conclusion that breaking detectors "is not an easy task" for these cases somewhat contradicts its own sweeping framing.

## Suggestions

- Restructure the abstract and introduction to clearly distinguish which results come from recursive paraphrasing (watermarking, retrieval-based) vs. single-round/multi-query T5 paraphrasing (zero-shot, neural network-based), rather than subsuming all under "recursive paraphrasing."
- Discuss the paraphraser capability requirement explicitly: under what conditions can a weaker paraphraser successfully attack a stronger target LLM? The T5-vs-GPT-2 Medium experiment provides some data, but this dimension needs explicit acknowledgment and analysis.
- Tighten the theoretical claims: instead of arguing detection is "fundamentally hard" or "cannot be achieved," state that the bound provides a ceiling on achievable performance and note that the bound is not proven tight, so actual detector performance may be significantly worse than the bound suggests.

## Score and Decision

The paper makes genuine and important contributions showing that watermarking and retrieval-based detectors are vulnerable to recursive paraphrasing, and that spoofing attacks are feasible. However, the overclaiming—conflating two different attacks under one banner in the abstract, and overstating what the theoretical result establishes about detection impossibility—are significant issues that mislead readers about what the evidence actually supports. The paper would be substantially stronger if its claims matched its evidence.

**Originality**: Moderate. The recursive paraphrasing idea and spoofing attacks are novel contributions, though the theoretical result is acknowledged by the authors as "not surprising."  
**Importance of research question**: High. AI text detection reliability is a timely and important problem.  
**Claims well supported**: Mixed. Core empirical results for watermarking and retrieval-based detectors are strong; claims about zero-shot/neural network detectors and theoretical hardness overreach the evidence.  
**Soundness of experiments**: Good for watermarking/retrieval; limited for neural network/zero-shot (different, weaker attack paradigm used).  
**Clarity of writing**: Generally clear, but the abstract/introduction framing is misleading about the attack methodology.  
**Value to community**: Moderate-to-high—the watermarking and retrieval-based attacks are valuable, but the overclaimed scope reduces trustworthiness.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>