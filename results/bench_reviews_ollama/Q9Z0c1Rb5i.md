Now I have a thorough understanding of the paper. Let me now carefully evaluate each of the harsh critic's claims against the actual paper.

**Harsh Critic Issue 1: Label-dependent concept annotations undermine the core CBM premise**

The paper says (line 77): "for each training image x whose ground truth label is y, we annotate it only with concepts that are involved in predicting y (as indicated by the intervention matrix)." This is indeed a fundamental change from standard CBMs where concept annotations are class-independent. The criticism is valid — if a concept is visually present but not associated with the ground truth class in T, it gets GT_c=0, which means the model is trained to predict it as absent even though it's visually there. This is a genuine philosophical shift that the paper does not explicitly acknowledge.

**Harsh Critic Issue 2: The "eliminating information leakage" claim is not supported by the theoretical argument**

The theoretical argument in Section 3.3 (lines 97-109) only considers the inference-time computation c*T and shows that label confidence differences depend only on unique concepts. It does NOT address training dynamics. The BCE loss uses label-dependent GT_c, and the CE loss provides gradients through T to c. The critic's argument that the CE loss can still push shared concepts c_i in class-differentiating ways via gradients is valid in principle. However, I need to think about whether this really matters. The theoretical argument is about the *structure* of label prediction (c*T is a simple sum that only depends on which concepts are active), not about what information c encodes. The claim that "no information beyond a and b's unique concepts is leveraged to classify them" at inference time is technically correct GIVEN the concept vector c — the multiplication c*T only uses c_i values. The real question is whether c itself encodes class information beyond what the concepts represent. The label-dependent supervision means c IS class-informed, but the paper's argument is about the label *prediction mechanism*, not about the concept *representation*. The paper's claim that the intervention matrix eliminates leakage in the label prediction pathway is structurally valid (c*T can only distinguish classes through unique concepts). But the critic's deeper point is that making concepts class-conditioned means the concepts themselves become a carrier of class information — which is a different kind of "leakage" from what the paper formally defines. The paper's definition of leakage is specific: "unintended and additional information beyond the predicted concepts is leveraged for the follow-up label prediction." If the concept predictions ARE class-conditioned (because they're trained with label-dependent supervision), then by the paper's own definition, the class information is "in the concepts" not "beyond the concepts." So technically, the paper's claim is consistent with its own definition. But this is a semantic sleight of hand — the concepts are no longer objective descriptors. This is a valid concern but I'd classify it as a philosophical/trade-off concern rather than a fatal flaw.

**Harsh Critic Issue 3: The Concept Removal metric does not measure reduced information leakage**

The critic argues that faster performance drop when removing concepts indicates concept *dependence*, not absence of leakage. Let me check the paper's actual argument (lines 163-172). The paper says: "if a CBM suffers from information leakage, removing concepts that contribute most to the label prediction should not notably undermine the CBM performance." The intuition is: if there's leakage, the model has alternative pathways beyond concepts, so removing concepts shouldn't hurt much. The critic's counter-argument is that a model could have leakage THROUGH its concepts and still show fast degradation when those concepts are removed. This is a reasonable concern, but it's somewhat contrived — if leakage is THROUGH concepts, removing the concepts removes the leakage too, which would hurt performance. Is that really "leakage through concepts"? The paper's definition says leakage is "beyond the predicted concepts," so if the information IS in the concepts, it doesn't count as leakage by definition. But the deeper issue is that label-dependent training has made the concepts themselves encode class information, and removing them naturally hurts. The metric is a reasonable (if imperfect) proxy, and the paper supplements it with Concept Locality and Concept Perturbation metrics. This is a minor-to-moderate concern.

**Harsh Critic Issue 4: Performance gains are not cleanly attributed**

The paper's main ablation is SUPCBM_FC (replacing T with a learned FC layer). This only tests the effect of the intervention matrix. The critic wants an ablation isolating label supervision from the intervention matrix. This is a valid request — the paper introduces multiple innovations simultaneously and the ablation doesn't disentangle all of them. The SupCBM_FC ablation does partially address this (it shows the fixed T matters vs. learned FC), but doesn't test whether label-dependent supervision alone would suffice. This is a moderate concern.

Now let me evaluate the Strength Finder's claims:

1. "Principled elimination of information leakage via the intervention matrix" — The case analysis in Section 3.3 is structurally sound for inference-time, but the claim of "elimination" is too strong given the training-time issues.

2. "Strong empirical performance surpassing SOTA CBMs across all datasets" — Valid, Table 1 shows consistent improvements.

3. "Multi-metric evidence of reduced information leakage" — Valid, three metrics are used. But the Concept Removal metric interpretation has the caveats discussed above.

The hierarchical concept design is a genuine strength. The post-hoc lightweight design is practical.

Let me also check the human study criticism: 11 CV PhD students is indeed a narrow evaluator pool, and 29/100 selections is not dominant. But the paper is transparent about this.

Now let me assemble the final review.</think>Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

The paper proposes SupCBM, a new CBM paradigm that addresses information leakage by (1) using label-dependent concept supervision (annotating images only with concepts relevant to their ground truth class per an intervention matrix T), (2) replacing the learned label predictor with a fixed binary intervention matrix that sums concept probabilities for each class, and (3) constructing a two-level hierarchical concept set (nounal perceptual + adjectival descriptive concepts) generated by GPT.

## Strengths

- **Consistent empirical gains over SOTA CBMs across four datasets**: Table 1 demonstrates SupCBM outperforms all compared CBMs (P-CBM, Label-free CBM, LaBo, Yan) on CIFAR-10, CIFAR-100, CUB-Bird, and HAM10000, and achieves comparable or superior performance to the Feat upper bound. This is a strong result for a post-hoc method.
- **Hierarchical concept set design is well-motivated**: The two-level structure (nounal perceptual concepts + adjectival descriptors along shape/color/size dimensions) naturally captures finer-grained semantics that flat concept sets miss. The fish example ("fan tail" vs. "veil tail" in Section 3.1) effectively illustrates this, and the approach yields better interpretability with fewer total concepts (3,236 vs. LaBo's 10,000).
- **Intervention matrix provides transparent, structurally intervenable label prediction**: Using a fixed binary matrix T for label prediction (c*T = sum of relevant concept probabilities) makes the concept-class association directly inspectable and editable — setting T[i,j] to 0/1 directly controls whether concept i influences class j (Section 3.2). This is structurally cleaner than intervening on a learned opaque label predictor.
- **Multiple leakage evaluation metrics**: The paper evaluates information leakage through three complementary metrics — Concept Removal (Fig. 2(a)), Concept Locality (Table 2, Appendix A), and Concept Perturbation (Table 3, Appendix A) — with SupCBM showing lowest leakage across all three.
- **Lightweight post-hoc conversion**: Training only a single CB layer (~30 minutes on one RTX 3090, Section 4) without modifying the backbone or training a label predictor makes the method practical for converting existing pretrained models.

## Weaknesses

### Fatal
None.

### Major

- **Concept annotations are label-dependent, fundamentally changing what concept predictions represent**: The paper annotates each training image *only* with concepts that the intervention matrix T associates with its ground truth label (Section 3.2: "we annotate it only with concepts that are involved in predicting y"). In standard CBMs, concept annotations are class-independent — a red bird image has "red"=1 regardless of whether the label is cardinal or robin. In SupCBM, if T doesn't associate "red" with the ground truth class, GT_c["red"]=0, and the model is trained to *not* predict red even though red is visually present. The concepts therefore become class-conditioned predictions of decision-relevance rather than objective descriptions of image content. This is a philosophical shift that the paper never explicitly acknowledges or evaluates. A user inspecting concept predictions to understand "what the model sees" would be misled, because the concepts reflect what the model was trained to see *for that class*. This matters because objective concept descriptions are the foundational interpretability promise of CBMs.

- **Incomplete ablations: performance gains cannot be cleanly attributed to the intervention matrix vs. label supervision**: SupCBM simultaneously introduces label-supervised concept annotations (label-dependent BCE loss + CE loss), a fixed intervention matrix T, and hierarchical concepts. The only ablation (SUPCBM_FC, Section 5.2.1) replaces T with a learned FC layer, showing the fixed matrix contributes something. But this does not isolate the effect of label-supervised concept annotation — the paper's most consequential design change. Without an ablation where concepts receive class-independent (standard CBM) supervision but label prediction uses T, the contribution attribution is unclear. The performance gap between SupCBM and baselines could largely come from the additional CE loss term and label-dependent annotations rather than from the intervention matrix or hierarchical concept structure.

### Minor

- **The "eliminating information leakage" claim (Section 3.3) is overstated relative to the evidence**: The theoretical argument in Section 3.3 only addresses inference-time computation (c*T can only distinguish classes through unique concept sums), but does not engage with training dynamics. The joint loss (ℓ_BCE + ℓ_CE) with label-dependent GT_c means concept representations c are shaped by class information during training. While the inference-time label prediction pathway is structurally constrained by T, the concept predictions themselves encode class information through the supervision procedure. The paper's definition of leakage ("information beyond the predicted concepts") makes the claim technically consistent but semantically thin — the concepts themselves have become the carrier of class information. The claim should be tempered to "significantly reduces information leakage in the label prediction pathway" rather than "eliminates information leakage."

- **The Concept Removal metric interpretation requires nuance**: The metric's logic (fast accuracy drop = less leakage) is sound as a first-order intuition and consistent with Mahinpei et al. (2021), but a model whose concepts are class-conditioned (as SupCBM's are) will naturally show fast degradation upon concept removal because the class information is fully routed through the concepts. This doesn't necessarily mean there's no leakage — it means the concepts themselves encode class-conditional information. The Concept Locality and Concept Perturbation metrics partially address this concern, providing complementary evidence.

- **SupCBM surpasses the Feat "upper bound" on CIFAR-10 without discussion**: The paper defines Feat as offering the "upper bound" performance of CBMs (Section 5.1), then reports SupCBM exceeds it on CIFAR-10. This deserves explanation — either Feat is not a true upper bound, or something about SupCBM's label-supervised training confers an advantage that goes beyond what CBMs should theoretically achieve.

### Trivial
None.

## Nice-to-Haves

- An ablation isolating label supervision from the intervention matrix (e.g., standard class-independent concept annotations with T-based label prediction, vs. label-supervised concepts with a learned FC predictor) to clarify which innovation drives the improvements.
- A concept fidelity evaluation measuring how well SupCBM's predicted concepts correspond to objective visual attributes, not just whether they produce correct labels — this would directly address the label-dependent annotation concern.
- Broader evaluator pool in the human study (11 CV PhD students is a narrow demographic for assessing general-user interpretability).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Model/tool availability concerns"**: Any implication that GPT-4, CLIP, or other cited tools are not available or cannot be independently verified — these are assumed to exist per the rules.
- **Formatting/presentation nitpicks**: The "pq-dimensional" notation ambiguity, missing standard deviations display issue — Section 4 explicitly states "report the mean and standard deviations of our results in Sec. 5," and Table 1 may display them in the image (extracted text can't confirm). The dimensionality notation is conventional for hierarchical concept structures.
- **"Harsh Critic Issue 2 in full"**: The claim that the theoretical argument is fundamentally flawed because CE gradients can push shared concepts in class-differentiating ways partially misunderstands the paper's argument. Section 3.3 is specifically about the *structural* properties of the label prediction pathway c*T at inference time, not about what c encodes. The valid core of this criticism — that the training procedure makes c itself class-informed — is captured under Minor weakness above.
- **Demand for comparison under matched supervision** (giving baselines the same CE loss term): This is scope creep — the paper's contribution is the full SupCBM package, and baselines have their own training procedures. The real issue is the missing ablation, which is already captured.
- **Prompt tuning claim without evidence**: The paper states "tuning the prompts does not affect the generated concepts" (Section 4). This is a minor empirical claim that doesn't affect the core contribution.
- **Human study limited to 11 CV PhD students and only 29/100 selections**: While 11 evaluators is small and the selection rate is not dominant, the paper is transparent about the setup. This is a nice-to-have improvement, not a weakness that threatens claims.
- **Strength Finder's claim about "principled elimination" via case analysis**: This is weakened by the training-time caveats discussed above and is moved to a tempered version in the minor weaknesses. The raw "proving that label prediction can only distinguish classes through unique concepts" overstates what a three-case informal analysis achieves.
- **Strength Finder's claim about SupCBM matching/exceeding Feat as strength without caveats**: While impressive, this contradicts the paper's own framing of Feat as an upper bound and raises questions that should be acknowledged rather than celebrated uncritically.

## Novel Insights

SupCBM reveals a fundamental tension in CBM design that the community has not adequately addressed: making concepts label-supervised reduces information leakage through the label prediction pathway but potentially undermines concept fidelity by making concept predictions class-conditioned rather than objective. This trade-off between "leakage-free label prediction" and "objective concept descriptions" deserves explicit recognition. The paper effectively solves one problem by shifting it elsewhere — the intervention matrix structurally constrains the label prediction pathway, but the label-dependent supervision means the concepts themselves become the channel through which class information flows. This is not necessarily wrong (it may be the right trade-off for many applications), but it redefines what CBM concepts mean, and the paper would be stronger for acknowledging this explicitly.

## Suggestions

- Add an explicit discussion of the label-dependent annotation trade-off: acknowledge that SupCBM's concept predictions are class-conditioned decision-relevance indicators rather than class-independent visual descriptions, and argue for why this is an acceptable or preferred trade-off for the target use cases.
- Add a simple ablation: train a standard CBM (class-independent concept supervision) but use the intervention matrix T for label prediction. This isolates the effect of the architectural innovation from the supervision change.

## Score and Decision

The paper makes genuine and empirically validated contributions — consistent accuracy improvements, a structurally leak-constrained label prediction pathway, and a well-motivated hierarchical concept design. The major weaknesses (label-dependent annotation trade-off unacknowledged, incomplete ablations) are significant but do not invalidate the contributions. The method works well in practice and the intervention matrix is a clean idea. The concerns are of the "this important caveat should be discussed" and "this ablation would strengthen" variety, not "the paper's core claim is wrong."

Originality: Good. The combination of label-supervised concepts + fixed intervention matrix + hierarchical concepts is novel for CBMs.
Importance of research question: High. Information leakage is a well-recognized problem in CBMs.
Claims support: Partially supported. The leakage reduction claim is overclaimed; the accuracy claim is well-supported.
Soundness of experiments: Good overall, but weakened by missing key ablation.
Clarity: Adequate, though the core trade-off is obscured.
Value to community: Good — the intervention matrix idea and hierarchical concept structure are useful regardless of the annotation debate.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>