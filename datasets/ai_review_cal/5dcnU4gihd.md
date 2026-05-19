- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes "Attention Head Purification" for adapting CLIP to domain generalization. The key idea is that not all attention heads in CLIP's ViT encoder are equally domain-generalizable. The method decouples purification into two levels: (i) **task-level purification** via head-aware LoRA (HA-LoRA), which assigns independent low-rank B matrices per attention head to avoid interference during adaptation, and (ii) **domain-level purification** via learnable gating (DIG) with MMD loss to emphasize domain-invariant heads. Experiments on five DG benchmarks show consistent improvements over strong baselines, and the method is orthogonal to prompt-learning techniques.

## Strengths

- **Novel empirical finding about attention head specialization for DG**: Figure 1 demonstrates that dropping the least "useful" heads (evaluated via multiple strategies — random, manual, cross-validation, adapt&drop) consistently improves DG accuracy, and attention maps confirm dropped heads focus on background while retained heads focus on objects. This observation goes beyond prior work's focus on avoiding catastrophic forgetting.

- **HA-LoRA's benefit is concretely demonstrated through the interaction with DIG**: Table 1 (Right) shows that with domain-invariant gating (DIG), HA-LoRA outperforms conventional LoRA by 1.0% on OfficeHome and 1.4% on DomainNet, while without DIG the gap is only ~0.1%. This directly supports the claim that per-head B matrices reduce head interference and make subsequent gating more effective.

- **Decoupling task-level and domain-level purification is empirically justified**: Table 3 (MMD ablation) systematically compares four configurations of where MMD gradients flow. Restricting MMD to gates only (the proposed design) achieves 87.0/61.1/98.1 on OH/DN/PACS, clearly outperforming alternatives where MMD also updates HA-LoRA or neither. This is concrete evidence for a non-obvious design choice.

- **Consistent improvements across prompt-learning methods**: Table 4 shows that adding attention head purification improves every prompt method tested (PromptStyler: +5.5%, CoOp: +4.7%, STYLIP: +2.1%, DUPRG: +5.2%), demonstrating orthogonality.

- **Practical efficiency**: Training time is 1h30min on DomainNet vs. 4h46min (CLIPood) and 5h24min (MIRO), with identical inference time (39s).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Zero-shot baseline inconsistency across tables**: The zero-shot DomainNet accuracy is reported as 57.7 in Table 1 (Left, first row) but 56.6 in Table 5 and Table 4 (Zero-Shot row). OfficeHome is consistent at 82.4. This 1.1% discrepancy for the same model without training is unexplained and could reflect sensitivity to prompt templates or evaluation batch construction. Since gains are measured against these baselines, inconsistency undermines precise interpretation of improvement margins.

- **MMD loss implementation omits kernel bandwidth**: The paper states "k denotes the Gaussian kernel" (Eq. 4, line 179) but never specifies the kernel bandwidth or how it is set (e.g., median heuristic, fixed value, tuned per dataset). MMD results can be sensitive to this hyperparameter. The α sensitivity is provided (Table Right in Table 5), but the kernel bandwidth is a separate nontrivial choice. This omission affects reproducibility.

- **"Ours" in the main comparison table stacks orthogonal components without decomposition**: In Table 5, "Ours" (79.0 avg) is attention head purification combined with PromptStyler prompt optimization. The core method without prompt learning achieves 78.2 avg (from Table 4), which is below the CLIPood original (78.6) and roughly on par with STYLIP/DSPL (77.8). The paper is transparent about this (caption: "For our method, we report numbers obtained by attention head purification combined with prompt learning"), but the table's layout visually suggests a larger margin than the core method alone supports. Separating the presentation of the core contribution from the stacked result would improve clarity.

- **Claim of "interference elimination" between heads lacks direct mechanistic evidence**: The paper attributes HA-LoRA's benefit to eliminating head interference (Section 3.2, line 201-202), but the only evidence is the performance correlation in Table 1 (Right). A direct measurement — e.g., showing that learned directions become more orthogonal across heads, or that gradient conflict decreases — would substantiate the mechanistic claim. As presented, the pattern is equally consistent with "more capacity per head" benefiting gating.

- **Statistical variance not reported**: The paper states results are averaged over three runs but provides no standard deviations or confidence intervals in any table. Given that several margins are small (e.g., 0.4% avg vs. CLIPood original), variance information is needed to assess whether differences are meaningful.

### Trivial

- **γ scaling factor in gating** (Eq. 3, line 167): The output is scaled by γ = number of heads to "compensate the scale changes after softmax operation." Since the subsequent layer (concat + projection) includes LayerNorm, the scaling may be unnecessary. A brief ablation or justification would clean up the design.

## Nice-to-Haves

- **Data contamination acknowledgment**: CLIP's training data likely overlaps with standard DG benchmarks (e.g., zero-shot PACS at 96.1% is suspiciously high). This is a general field-wide limitation affecting all CLIP-based methods, not a flaw of this paper specifically, but acknowledging it and perhaps evaluating on a held-out distribution (e.g., ImageNet-Sketch) would strengthen credibility.

- **Deeper discussion of why MMD on HA-LoRA hurts performance**: The paper says "coupled optimization is more difficult" (line 292) but does not develop a concrete hypothesis (e.g., MMD's invariance objective conflicts with the contrastive loss's discriminative objective at the feature level). The empirical evidence (Table 3) is clear, but the reasoning is vague.

- **Ablation of gating placement**: Gating is applied to attention outputs after scaled dot-product attention. An ablation showing why gating queries/keys/values directly is less effective would strengthen the design rationale.

## Removed Points

These points were raised in reviews but do not survive verification against the paper:

1. **"Cross-validation motivation is partly circular"**: The critic argues that the Figure 1 cross-validation strategy (learning gates via Gumbel-Softmax) is similar to DIG, making the observation self-fulfilling. This misunderstands the purpose — the experiment uses *four* distinct strategies (random, manual, cross-validation, adapt&drop), all showing improvement from dropping heads. The observation is robust across evaluation methods, not dependent on the cross-validation approach. *[Reason: Factually incorrect assessment of experimental design.]*

2. **"STYLIP/DSPL comparison is unfair because they are standalone prompt methods"**: STYLIP and DSPL *are* prompt-learning methods themselves. Comparing "purification + PromptStyler" against "STYLIP (which uses its own prompt optimization)" is comparing two prompt-learning-based approaches. The comparison is standard practice; the paper also separately reports core method performance. *[Reason: Overstated; comparison is valid and paper is transparent.]*

3. **"Data contamination is not acknowledged (evidential concern)"**: The critic frames this as a critical issue, but it applies equally to all CLIP-based DG methods and is outside the paper's stated scope. The paper is about attention head purification as a technique, not about decontaminating CLIP's pretraining data. *[Reason: Scope creep — applies universally to the field, not specifically to this paper's claims.]*

4. **"CLIPood reproduction is lower than original"**: The paper reports both original and reproduced numbers (marked with †), which is transparent. The reproduction difference could reflect standard practice differences (batch size, epochs). *[Reason: The paper already handles this transparently; the criticism doesn't identify a flaw in the paper's method.]*

## Novel Insights

The reviews surface one genuinely novel synthesis: the observation that the *interaction* between HA-LoRA and DIG (Table 1 Right) is the key to the method's success — HA-LoRA alone barely outperforms standard LoRA (+0.1-0.2%), but with DIG the gap jumps to +1.0-1.4%. This suggests that per-head parameterization is not primarily about better per-head adaptation, but about enabling the gating mechanism to make crisper head-level decisions. The paper attributes this to "interference elimination," and while the mechanistic claim lacks direct evidence, the empirical interaction pattern is the paper's most interesting finding.

## Suggestions

1. Add standard deviations to all main tables, especially given small margins vs. original CLIPood.
2. Specify the MMD kernel bandwidth (or the heuristic used to set it) for reproducibility.
3. Add a footnote or visual cue in Table 5 clearly separating the core method (78.2 avg, no prompt optimization) from the stacked result (79.0, with PromptStyler), so readers can immediately see each contribution.
4. Resolve the 57.7 vs. 56.6 zero-shot DomainNet discrepancy with an explanation or consistent reporting.
5. If possible, add a direct measure of head interference (e.g., cosine similarity of learned update directions across heads) to strengthen the mechanistic claim about HA-LoRA.
