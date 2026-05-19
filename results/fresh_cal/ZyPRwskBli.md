Now I have the full paper content from the initial read and have verified specific claims. Let me produce the consolidated review.

## Summary

This paper proposes EDT (Efficient, Data-free, Training-free), a backdoor attack on large pre-trained vision models that uses a codebook (key-value lookup table inserted between the encoder and downstream layers) to replace the full image embedding with a target embedding whenever a trigger patch is detected. The attack requires no access to training data and no gradient-based training — the codebook is built by encoding a few trigger patches and target images. Experiments on ViT, CLIP, BLIP, and Stable Diffusion across classification, captioning, and generation tasks report 100% attack success rates with zero clean accuracy drop (for the grey trigger), and the paper also shows improved OOD accuracy that helps rationalize the codebook's presence.

## Strengths

1. **Consistent 100% ASR with zero clean accuracy drop (grey trigger).** Table 1 shows EDT-grey achieves 100% ASR on ViT, CLIP-ViT32, and CLIP-ResNet50 across CIFAR-10, GTSRB, and ImageNet, with ΔCA = 0.00 on every combination. This directly demonstrates that the method satisfies the paper's stated goal of a backdoor that does not degrade benign performance.

2. **Truly training-free and data-free.** Section 3.2 describes codebook construction using only a trigger patch and a single target image — no original training data and no gradient computation. Table tab:time (training time comparison) confirms EDT requires 0.00 hours, while baselines require up to 19.47 hours on ImageNet.

3. **Generalizability across architectures and tasks.** The method is demonstrated on ViT (classification), CLIP (classification), Stable Diffusion (generation, Figure 3), and BLIP (captioning, Table tab:caption). This breadth shows the approach is not tied to a single architecture.

4. **Domain-adaptation improvement partially supports the stealth claim.** Table tab:adaptation shows accuracy on ImageNet-Sketch rising from 41.65% → 50.29% (ViT) and 44.59% → 45.57% (CLIP) after codebook injection, providing concrete evidence that the codebook can be positioned as a beneficial module rather than purely malicious.

5. **Principled formulation of attack desiderata.** Section 2.2 introduces three specific properties (stealthy/model-agnostic, data-free, training-free) plus a bonus property (multi-trigger). This conceptual framing clearly distinguishes the paper's setting from traditional backdoor attacks.

## Weaknesses

### Fatal

None.

### Major

- **Overclaimed comparison to baselines under different constraints.** The paper states it "outperforms the state-of-the-art" (line 30) and the title claims "Unlocking Vulnerabilities." However, EDT operates through a fundamentally different mechanism than the baselines (BadNets, fine-tuning, TrojanNet) — those modify model parameters via training on poisoned data, while EDT inserts an untrained lookup table. The comparison is apples-to-oranges on metrics like ASR, ΔCA, and training time, since EDT's advantages (100% ASR, 0 training time) are largely *consequences of the different approach*, not evidence of superior attack capability within the same threat model. The paper would be stronger if it explicitly acknowledged this incomparability and focused evaluation on what makes the attack nontrivial: detection resistance and practicality under its own threat model.

### Minor

- **Missing ablation of the matching threshold ε (cosine similarity threshold).** The method (line 144) uses cosine similarity with a threshold ε to decide whether a patch embedding matches a stored key, but ε is never specified, ablated, or discussed anywhere in the paper. This is a critical parameter: too high and the trigger may not fire; too low and false positives occur. The paper's own explanation of the white trigger's 0.68% ΔCA (line 250: "some clean images initially have a similar pure white square at the last patch") highlights exactly this issue, yet no analysis of how ε affects false positive/false negative rates is provided.

- **Behavior when multiple patches match different keys is unspecified.** The pipeline (lines 142–153) checks if "any" patch matches a key. When the image contains multiple triggers matching different keys (e.g., in the multi-trigger setting, Table tab:multi-trigger), it is unclear which value is used — first match, last match, or some other resolution strategy. This matters for both correctness and potential collisions.

- **No quantitative metric for image generation quality.** The Stable Diffusion experiments (Section 4.2, Figure 3) show only qualitative examples and T-SNE plots. No FID, IS, or other standard metric is provided to quantify either the generation quality on clean inputs or the attack success rate (percentage of images that are cats). This makes the generation evaluation substantially weaker than the classification evaluation.

- **Domain adaptation evidence is thin.** Table tab:adaptation shows improvement on only one OOD dataset (ImageNet-Sketch). No standard domain adaptation baselines (e.g., zero-shot CLIP, few-shot adapters) are compared, so it is unclear whether the 20% gain on ViT is competitive or merely a demonstration of concept. The claim that this "rationalizes the codebook" would be much stronger with a broader evaluation.

- **Notational inconsistency in the matching formulation.** Line 144 defines `EDT(z_i) = {𝟙|sim(z_i,k) > ε}`, but line 150 conditions on `f_θ(x_{ij}) = k ∈ K and INDEX(k) ∈ L`. The first formulation checks the *overall* embedding against keys; the second checks *patch* embeddings against keys. These describe different matching strategies, creating confusion about the actual implementation.

### Trivial

- The CIDEr AA_p value of 10.00 (Table tab:caption) is unusual — CIDEr scores are typically ≤ 1 for standard implementations. This may be a scaling issue or a different CIDEr variant, but it should be clarified.

## Nice-to-Haves

- A comparison against other *data-free* or *training-free* backdoor injection methods (if any exist), or an explicit statement that none exist and why comparison to training-based methods is still meaningful.
- An analysis of codebook detectability via structural defenses (e.g., model diffing, pruning-based removal, fine-tuning survival). The current defense evaluation tests only runtime behavior detection (STRIP, Scale-UP).
- Scalability analysis: inference-time overhead as the number of trigger/OOD entries grows, and behavior when hundreds of triggers are injected.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The method is not a backdoor attack in the standard sense."** The paper explicitly proposes *new properties* for backdoor attacks in the era of large pre-trained models (Section 2.2) and defines a new threat model (Section 2.3). Rejecting the paper on the grounds that it does not fit the *traditional* definition ignores its stated contribution. Removed because it misreads the paper's framing.

- **"The 100% ASR is tautological."** Many backdoor attacks achieve near-perfect ASR by design; this does not invalidate the method. The contribution is in *how* it is achieved (training-free, data-free), not the ASR number alone. Removed as it dismisses the core claim without justification.

- **"CIDEr 10.00 is suspicious / likely a formatting issue."** Speculation without evidence from the paper. The paper may use a non-standard CIDEr implementation; absent confirmation of error, this is not a valid weakness. Removed as unsubstantiated.

- **"Training time comparison (Table 8) is meaningless."** The comparison demonstrates that EDT satisfies Property 3 (training-free), which is a core claim. The fact that EDT requires 0 hours *is the point*. Removed as it ignores the purpose of the comparison.

- **"The defense methods' failure is unsurprising."** This is the reviewer's opinion, not a verifiable flaw. The paper demonstrates that two established detection methods fail against EDT, which is empirical evidence regardless of whether the reviewer finds it surprising. Removed as speculative.

- **Other nitpicks about "variety of models being limited"** — the paper tests four different architectures across three tasks, which is reasonable scope for a single paper.

## Novel Insights

The two reviews largely surface the same tension: EDT achieves its goals perfectly under its own assumptions, but those assumptions (white-box access to insert a codebook module) make the comparison to traditional backdoor attacks strained. The novel insight from reviewing is that the paper's strongest evidence is not the 100% ASR (which is an architectural consequence), but rather the domain adaptation improvement mechanism — this is the only part of the evaluation that addresses the *stealth* claim from a motivational angle rather than a technical one. Neither review fully grapples with whether a codebook that visibly improves OOD accuracy would actually evade suspicion in practice, which is ultimately a social/contextual question that may be outside the scope of a technical paper but is central to its threat model.

## Suggestions

1. **Clarify the threat model more sharply.** Explicitly state that the comparison to traditional baselines is only on the *output metrics* (ASR, CA preservation) and acknowledge that the mechanisms are different. Frame "outperform" as "achieves the proposed properties (data-free, training-free) that baselines cannot."

2. **Ablate the threshold ε and discuss false-positive rates.** Show how ε affects clean accuracy vs. attack success, and provide guidance for selecting ε given a trigger pattern.

3. **Specify the multi-match resolution policy.** Clarify what happens when multiple patches match different keys — first-match, all-match, or conflict resolution.

4. **Add quantitative metrics for image generation** (e.g., FID for quality, percentage of target-class generations for attack success).

5. **Expand the domain adaptation evaluation** with at least one standard baseline (e.g., linear probe, zero-shot CLIP) and more OOD datasets to strengthen the "rationalization" argument.

## Score and Decision

The paper identifies a genuine limitation of traditional backdoor attacks on large pre-trained models (data and training dependency) and proposes a simple, effective workaround via model editing. The experiments are reasonably broad across tasks and architectures, and the core result (100% ASR, 0% ΔCA with a training-free/data-free approach) is cleanly demonstrated. However, the evaluation has notable gaps — missing threshold analysis, unclear multi-match behavior, thin defense analysis, and overclaimed comparisons to baselines that operate under fundamentally different constraints. The technical novelty is incremental (applying the GRACE model-editing paradigm to backdoor attacks), but the problem framing and property formulation provide useful conceptual grounding. These weaknesses are addressable in revision and do not invalidate the core contribution, but they prevent the paper from being a strong accept in its current form.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>