Now I have a thorough understanding of the paper and can verify all claims. Let me produce the consolidated review.

## Summary

This paper proposes ConvINT, a semi-structured intention framework that decomposes conversational user intentions into four aspects (situation, emotion, action, knowledge), and WeRG, a weakly-supervised reinforcement learning fine-tuning method that generates ConvINT annotations at scale by combining coarse (rule-mapped), mid (LLM-annotated), and fine (human-annotated) data with tiered quadruple rewards. The paper evaluates ConvINT annotation quality and downstream response generation on DuRecDial and ESConv, showing that ConvINT annotations improve LLM-based response generation.

## Strengths

- **Large downstream gains from ConvINT are clearly demonstrated**: Table 4 shows that integrating ConvINT with ChatGPT on DuRecDial raises the success rate from 9.2 to 20.0 and reduces average turns from 10.55 to 1.87, directly showing that the framework helps LLMs steer dialogues toward goals more effectively.

- **WeRG outperforms all prompting baselines on both automatic and human evaluation of ConvINT quality**: Table 1 shows WeRG surpasses few-shot CoT on every metric across both datasets (e.g., DuRecDial F1 0.769 vs 0.711, BERTScore 0.941 vs 0.926). Table 2 reports large margins in human-rated informativeness, understanding, and conciseness (e.g., DuRecDial Informativeness 5.02 vs best baseline 3.96), confirming generated annotations are substantively better than prompt-based alternatives.

- **Ablation studies isolate the contribution of each WeRG component**: Table 3 shows that removing any single data source (coarse, mid, or fine) or the quadruple reward hierarchy lowers generation quality (e.g., removing mid supervision drops F1 from 0.769 to 0.728), providing direct evidence that the proposed weak-supervision combination and tiered reward are both necessary.

- **Scalability is demonstrated by increasing fine-annotated data proportion**: Figure 3 shows that raising human annotations from 10% to 30% yields consistent improvements, indicating the method can productively absorb more high-quality data.

- **ConvINT is grounded in cognitive theory**: Section 3.2 explicitly cites semantic pointers (Eliasmith, 2013; Blouw et al., 2016) and Schröder et al. (2014) to define the four-aspect decomposition, providing a theoretical basis that distinguishes ConvINT from ad hoc ontology designs.

## Weaknesses

### Fatal
None.

### Major

- **Missing critical experimental details make the method irreproducible**: The paper never specifies (1) which LLM is used as the policy model π_θ for WeRG training — it only says "LLMs" and "LLM policy π_θ"; (2) the actual reward values r_c — the paper says "simple scalar rewards" with "r_coarse < r_mid < r_fine" and "meticulously calibrated" but gives no numbers; (3) what RL algorithm (PPO, REINFORCE, or the closed-form DPO-style solution from Eq. 5) is used to optimize the objective. The paper also does not specify how the quadruple reward components (r_s, r_e, r_a, r_k) are computed per aspect — are they binary, real-valued, per-token, or per-sequence? These omissions prevent reproducibility and verification of the results.

- **No comparison against fine-tuning baselines for WeRG**: The ConvINT generation baselines (Table 1) are only prompting methods (Direct Prompt, CoT Prompt) without any fine-tuning. Since WeRG is a fine-tuning method, the evaluation cannot isolate whether WeRG's performance comes from its specific design (tiered quadruple reward, weak-supervision data mix) or merely from fine-tuning an LLM on any relevant data. The ablation study (Table 3) removes components of WeRG but never tests a simple SFT baseline on the same data mix or an RL baseline without the quadruple reward decomposition. This limits what the paper can claim about WeRG's superiority as a fine-tuning strategy.

### Minor

- **Downstream experiments do not isolate whether improvement comes from ConvINT's specific structure vs. any additional context**: The paper shows ConvINT+ChatGPT > ChatGPT alone (Table 4), but does not compare ConvINT against alternative intention representations (e.g., structured slot-values from existing CU models, or free-text summaries). While the per-aspect removal experiment (Table 5) shows each aspect contributes, the core claim that ConvINT's *specific semi-structured four-aspect design* is superior to other representations is not directly tested in downstream tasks.

- **Human evaluation is limited in scale and statistical rigor**: Only three student annotators rated 50 conversations per dataset. Fleiss' Kappa (0.2–0.6) indicates fair-to-moderate agreement, suggesting noisy annotations. The paper reports average scores without variance, confidence intervals, or significance tests. For claims about "high-quality" data generation, a larger-scale evaluation with significance testing would strengthen the conclusions.

- **Automatic metrics for ESConv response generation may not capture the relevant quality dimensions**: Table 5 reports F1, BLEU-1/2, BERTScore, and BARTScore for emotional support dialogue response generation. These lexical and semantic overlap metrics are known to correlate poorly with quality in open-ended generation, especially for emotional support where appropriateness and empathy matter more than n-gram overlap. The paper would benefit from task-specific metrics or human evaluation of response quality on ESConv.

- **No significance tests or variance estimates reported anywhere**: Tables 1–5 report point estimates without standard deviations, confidence intervals, or p-values. Some differences between methods in Table 1 appear modest (e.g., BARTScore 0.32 vs 0.35 on DuRecDial), making it unclear whether observed differences are meaningful.

### Trivial
None.

## Nice-to-Haves

- Compare WeRG against SFT on D_fine only, SFT on D_WeRG without reward weighting, and RL with a single scalar reward per instance (no aspect-level decomposition) to isolate the benefit of each design choice.
- Compare ConvINT against alternative intention representations (structured slot-values, free-text summaries) in downstream tasks to validate that the specific four-aspect semi-structured form drives improvement.
- Include computational cost comparison (training time, annotation cost) across methods.
- Use emotion-specific evaluation metrics (e.g., empathy ratings, user satisfaction) for the ESConv downstream task.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism that theoretical grounding is "superficial" and aspects "chosen ad-hoc"**: The paper explicitly grounds ConvINT in semantic pointers theory (Eliasmith, 2013; Blouw et al., 2016) and Schröder et al. (2014) with a direct definition. This is a strawman — the paper does provide theoretical grounding, and the critic's characterization is inaccurate.

- **Criticism about not exploring 1%/5% fine-annotated data proportions**: Scope creep — the paper's chosen range (10%–30%) is reasonable and demonstrates scaling behavior; requesting smaller proportions is not a genuine weakness.

- **Criticism about not reporting annotation/computational cost**: A nice-to-have, not a core weakness.

- **Criticism about not comparing against existing CU models (intent-slot detectors)**: The paper's framing is about intention *representation* for LLMs, not a new intent-slot detector. This comparison is outside the stated scope.

- **Criticism about the related work section being generic**: This is a presentation observation about the literature review, not a weakness of the paper's contribution or evaluation.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify all missing experimental details**: State the LLM backbone used for WeRG training, the exact reward values for each tier (coarse/mid/fine) and each aspect (situation/emotion/action/knowledge), and the RL algorithm (or the optimization procedure if using the closed-form solution from Eq. 5). Without these, the method cannot be reproduced.

2. **Add fine-tuning baselines**: At minimum, compare WeRG against SFT on D_fine only and SFT on D_WeRG without reward weighting. This would isolate the benefit of the weak-supervision mix and the tiered reward.

3. **Add alternative representation comparison in downstream**: Compare ConvINT against structured slot-value outputs and unstructured free-text summaries to validate that the specific four-aspect semi-structured design drives improvement, not just additional context.

4. **Report variance/confidence intervals**: Add standard deviations or confidence intervals to all tables to enable assessment of result stability.

5. **Expand human evaluation**: Increase the sample size and report per-item variance, with significance tests between methods.

## Score and Decision

**Originality** (6/10): The ConvINT framework and WeRG method are novel combinations of existing ideas (cognitive theories of intentions, weak supervision, RL fine-tuning), but the individual components (coarse-to-fine data mixing, tiered rewards) are not fundamentally new.

**Importance of research question** (7/10): Improving intention understanding for conversational AI is an important problem, especially for LLM-based systems.

**Claims support** (4/10): The central claim that WeRG generates high-quality ConvINT annotations is only supported against prompting baselines, not against alternative fine-tuning strategies. The downstream claim that ConvINT helps response generation is supported, but the specific advantage of ConvINT's structure over other representations is not isolated.

**Soundness of experiments** (4/10): The experimental design has significant gaps — weak baselines, missing control conditions, no significance testing, and missing implementation details that prevent verification.

**Clarity of writing** (6/10): The paper is generally well-written and the framework is clearly described, but critical implementation details are omitted.

**Value to the research community** (5/10): The ConvINT framework and WeRG-generated dataset could be valuable resources, but the current evaluation is insufficient to establish their reliability or superiority over alternatives.

The paper addresses an important problem and proposes a reasonable framework. However, the evaluation does not adequately support the claims due to (1) missing critical implementation details that prevent reproducibility, (2) weak baselines that do not include alternative fine-tuning methods, and (3) lack of controls isolating ConvINT's specific structure over other representations. These are addressable issues, but as presented the evidence is insufficient.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>