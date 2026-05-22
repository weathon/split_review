Now I will produce the final consolidated review.

---

## Summary

This paper expands machine unlearning by decoupling class labels from target concepts, introducing three "mismatch" scenarios (target, model, data) where the forgetting request does not align with the training taxonomy. It proposes TARF, a framework combining annealed gradient ascent on the forgetting set with target-aware gradient descent on identified hard-to-affect retaining data, guided by a theoretical analysis of "representation gravity." The model-mismatch evaluation is well-executed and shows clear improvements over baselines. However, for target/data mismatch the evaluation has a significant gap: the paper claims to forget the broader target concept (e.g., "people") but only measures unlearning accuracy on the given forgetting subset (e.g., "boy," "girl"), while the Retrained reference and TARF both retain high accuracy on other classes belonging to the same target concept.

## Strengths

1. **Novel problem framing.** The taxonomy of mismatch scenarios (target, model, data) provides a clear conceptual framework for unlearning requests that do not align with training labels. This is a genuine expansion of the unlearning literature beyond the conventional all-matched setting. (Section 1, Figure 1)

2. **Theoretical analysis of representation gravity.** Theorem 3.2 and Assumption 3.1 formalize how representation distance between data subsets influences forgetting dynamics, explaining why naive methods fail under mismatch. The bound in Eq. (2) connecting loss dynamics to representation distance is principled and supported by the empirical t-SNE and loss plots in Figure 3. (Section 3.2)

3. **Strong results on model-mismatch forgetting.** The fine-grained evaluation in Table 2 (UA-F on forgetting data and UA-R on retaining data within the same superclass) demonstrates that TARF properly disentangles entangled representations. On CIFAR-100 model mismatch, TARF achieves a Gap of 1.36, substantially lower than the next-best method (L₁-sparse at 2.65). This scenario is properly evaluated. (Table 2, Section 4.2)

4. **Real-world applications beyond image classification.** The paper demonstrates TARF for concept removal in Stable Diffusion (Figure 6) and information removal in LLMs (Table 5 on TOFU), supporting generality.

5. **Ablation studies validating design choices.** Figure 7 examines the effects of initialized strength \(k\), annealing schedules, different architectures, and gradient operations on identified false retaining data, providing practical insight into the method's behavior.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation does not measure concept-level forgetting for target/data mismatch.** The paper claims to forget the target *concept* (e.g., the superclass "people" in Figure 1), but Unlearning Accuracy (UA) is measured only on the *given forgetting subset* \(\mathcal{D}_f\) (e.g., "boy," "girl"). This is confirmed by the Retrained reference having UA=0.00 in Table 3 for target/data mismatch—if UA were measured on the full target concept \(\mathcal{D}_t\) (which includes false retaining data \(\mathcal{D}_{fr} = \) {"man," "woman," "baby"}), the Retrained would have non-zero UA since it was trained on \(\mathcal{D}_{fr}\). Retaining Accuracy (RA) stays high (\(\sim\)97%) for TARF in target/data mismatch, meaning the model still correctly classifies the false retaining data that belongs to the target concept. The Gap metric compares against a Retrained reference that itself has not forgotten the target concept (it is trained on \(\mathcal{D} \setminus \mathcal{D}_f\), which still contains \(\mathcal{D}_{fr}\)), so a small Gap does not demonstrate concept-level forgetting. The paper needs to either (a) report accuracy on \(\mathcal{D}_{fr}\) (false retaining data) separately to show the full target concept is forgotten, or (b) construct a Retrained reference that excludes all target-concept data \(\mathcal{D}_t\), or (c) reframe the claims to match what is actually evaluated—forgetting of the given subset with awareness of the broader concept. (Section 2 defines \(\mathcal{D}_{fr}\); Section 4.1 defines UA; Table 3 reports results; Section 1 claims "unlearn 'people'")

2. **The Retrained reference for target/data mismatch is not a proper "forgotten-concept" baseline.** The paper states "the retrained model for every task is trained using \(\mathcal{D}_r = \mathcal{D} \setminus \mathcal{D}_f\)." For target/data mismatch, this Retrained model still contains all false retaining data \(\mathcal{D}_{fr}\) from the target concept. This means the "gold standard" for comparison has not itself forgotten the target concept, making Gap values uninformative about concept-level forgetting. A proper reference would be trained on \(\mathcal{D} \setminus \mathcal{D}_t\) (excluding all data belonging to the target concept). (Section 2, line 73)

### Minor

1. **TARF identifies but does not actively forget false retaining data.** In Phase II, false retaining data are merely *excluded* from gradient descent (via \(\tau=0\) in Eq. 5) rather than actively unlearned via gradient ascent. The ablation in Figure 7 (right panel) explores this choice and suggests gradient cleaning may improve RA, but the paper does not fully justify why exclusion alone is sufficient for concept-level forgetting. This is less a flaw than an incomplete characterization. (Section 3.3, Eq. 5; Section 4.3, right panel of Figure 7)

2. **The assumption about known class count in the target concept is used in the evaluation setup.** Section 2 states "we assume that the number of classes in \(\mathcal{D}_{un}\) belonging to the target concept is known in target mismatch forgetting." While the method itself uses accuracy-drop ranking (Phase I) and does not strictly require this knowledge, its use in the evaluation setup is a limitation for practical deployment scenarios where this information is unavailable. (Section 2, line 73)

3. **Duplicate Remark numbering.** Remark 3.3 appears twice (lines 138 and 198), where the second instance should be Remark 3.4.

### Trivial
None.

## Nice-to-Haves

- **Report accuracy on false retaining data (\(\mathcal{D}_{fr}\)) separately for target/data mismatch.** A simple additional column (e.g., "UA on \(\mathcal{D}_{fr}\)") in Table 3 would clarify whether the model truly forgets the broader concept.
- **Construct an alternative Retrained reference for target/data mismatch** that trains on \(\mathcal{D} \setminus \mathcal{D}_t\) (excluding all target-concept data). This would provide a meaningful upper bound on forgetting.
- Include t-SNE plots of the *final* TARF-unlearned representations for target/data mismatch, similar to Figure 3 but after unlearning, to visually show whether false retaining class representations are pushed away.
- Vary the identification threshold \(\beta\) systematically to demonstrate robustness.

## Removed Points

The following points from the inputs were removed (with justification):

- **"No ablation on β in the main text"** — Removed because the appendix (which likely contains this ablation) was stripped by the PDF parser; the paper should not be penalized for content known to exist in the full submission.
- **"The method does not actively force forgetting of identified false retaining data" framing as a fatal flaw** — Demoted to Minor (above) because the paper's ablation in Figure 7 explicitly explores this design choice, and the method's goal is retraining approximation, not maximal forgetting.
- **"Missing related works"** — Removed as unverifiable without external sources.
- **Generic formatting/style nitpicks** — Removed as parser artifacts.
- **Strengths Finder strength about "this paper addressed an important problem"** — Removed as generic/superficial.

## Novel Insights

The most striking observation to emerge from the reviews is a tension in the paper's own framing: the "gravity effects" theory (Theorem 3.2) predicts that forgetting a subset of a concept will have weak spillover effects on semantically related but representationally distant subsets of the same concept. If this is true, then the claim of forgetting the broader target concept (e.g., "people" from only "boy"/"girl") faces an inherent theoretical obstacle—the gravity bound itself predicts the false retaining data will be *hard to affect*. The paper's Phase I identification exploits this same gravity effect to find false retaining data, but Phase II merely excludes them from gradient descent rather than applying the stronger gradient-ascent operation needed to overcome the gravity obstacle. Reconciling the theoretical prediction (weak spillover) with the empirical claim (concept-level forgetting) would strengthen the paper considerably.

## Suggestions

1. **For target/data mismatch, add a column to Table 3 reporting accuracy on \(\mathcal{D}_{fr}\) (false retaining data)** — or equivalently, separate RA into RA on \(\mathcal{D}_{fr}\) and RA on \(\mathcal{D}_r\). This single change would resolve the core evaluation gap.
2. **Train and compare against a Retrained reference that excludes all target-concept data \(\mathcal{D}_t\)** for the target/data mismatch setting. This would set a proper "forgotten-concept" baseline.
3. **Clarify the scope of the claim.** If TARF is designed to forget only the given subset \(\mathcal{D}_f\) while identifying and protecting the broader concept's remaining data from excessive forgetting, this is still a valuable contribution and the evaluation in Table 3 would be appropriate. The paper should state this explicitly rather than claiming to "unlearn 'people'."

---

## Score and Decision

The paper introduces a genuinely novel taxonomy and a theoretically grounded framework, with a properly executed evaluation for model mismatch and solid real-world demonstrations. However, the evaluation gap for target/data mismatch means the empirical claims about forgetting the target concept are not supported for two of the three new tasks. This is a significant weakness but not fatal—the conceptual, theoretical, and model-mismatch contributions stand independently. With proper additional evaluation (e.g., reporting accuracy on false retaining data), the empirical contribution could be completed. In its current form, the paper's conclusions are overclaimed relative to the evidence presented.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>