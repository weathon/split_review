- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 1, 5
Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes SolidMark, a method that augments training images with random grayscale borders and then uses the model's ability to reconstruct the border at evaluation time as a per-image indicator of pixel-level memorization. The paper also provides an analysis of weaknesses in existing memorization metrics (modified ℓ₂ distance, percentile-based scoring) and re-evaluates existing mitigation techniques using SolidMark.

## Strengths

- **Principled analysis of existing metric weaknesses (Section 3)**. The paper provides concrete visual evidence that the modified ℓ₂ distance still reports monochromatic images as false positives (Figure 2), and demonstrates how 95th-percentile scoring can conceal large reductions in the similarity distribution (Figure 3). These examples are specific, reproducible, and convincingly show real limitations in current practice.

- **Core design decouples key from content (Section 4)**. SolidMark embeds a random scalar key as a grayscale border that is semantically unrelated to the image content. This cleanly solves two problems that plague inpainting-based approaches: the key cannot be inferred from context, and the scalar distance function avoids the pitfalls of pixel-level distance metrics on image regions. This is a genuinely novel contribution.

- **Fine-grained pixel-level detection empirically confirmed (Table 5)**. The augmentation experiments show that even minor perturbations—cropping, rotation, or blurring that are sometimes barely visually perceptible—sharply reduce the model's ability to recall the border color, especially at tight thresholds δ. This provides direct evidence that SolidMark captures pixel-exact rather than semantic memorization, which is the paper's central technical claim.

- **Robustness to data duplication with independent keys (Table 3)**. The paper demonstrates that SolidMark still reports increased memorization when duplicate images are assigned different random borders, alleviating a natural concern that the method would miss duplication-induced memorization.

- **Public release of a pretrained foundation model (Section 5.4)**. Training and releasing SD 2.1 from scratch on a 200k LAION subset with SolidMark borders enables independent replication and lowers the barrier for others to use the method.

## Weaknesses

### Fatal
None.

### Major

- **Uncontrolled comparison in mitigation re-evaluation (Table 4, Section 5.3).** The paper compares SolidMark's results on SD 2.1 *fine-tuned on LAION-5K with borders* against SSCD results from Somepalli et al. (2023b) which used *standard SD 2.1 without borders*. The two models differ in training data, training procedure, and the presence of the border artifact. Any observed difference in mitigation effectiveness could be due to these confounds. The paper speculates that "reconstructive memorization likely arises more from cues in the prompt" but provides no controlled experiment where both metrics are applied to the same model and same generations. This makes the headline result of Section 5.3—that SolidMark contradicts prior findings—difficult to interpret as a clean comparison. A proper evaluation would apply both metrics to the same set of generations from the same model.

- **False positive rate is acknowledged but not quantified (Section 6).** The paper correctly notes that "our evaluation method has a false positive probability based on the chance of an unmemorized color randomly fitting to the key of a specific image," but provides no bound, simulation, or analysis of this rate. Since the method's main selling point is per-image evaluation, a false-positive analysis is essential for interpreting the reported memorization counts (e.g., how many of the reported memorizations at δ=0.01 are expected by chance across 10,000 images?). Without this, the reader cannot assess the reliability of the method's quantitative outputs.

### Minor

- **Framing overclaims the generality of SolidMark.** The abstract and introduction present SolidMark as "a novel evaluation method" and "a new method for precise evaluation of pixel-level memorization" without making clear that it requires the model to be trained (or fine-tuned) on border-augmented images. While the method section clearly describes the training requirement, and the paper releases a pretrained model to mitigate this, the framing in the abstract could mislead readers into expecting a post-hoc evaluation tool applicable to arbitrary pre-trained models. A small reframing to emphasize that SolidMark is a *training-time augmentation framework* that enables per-image memorization testing would better match the actual contribution.

- **No confidence intervals or significance tests.** The experimental results (Tables 2, 3, 4, 5) report point estimates with no measure of variability. Given the relatively small counts (e.g., percentages out of 10,000 images), variance could be non-trivial. For example, the claim that mitigation techniques produce "no meaningful difference" in Table 4 would be strengthened by bootstrapped confidence intervals or a statistical test.

### Trivial

- The word "non-intrusive" in the impact statement (line 180) is a stretch given that SolidMark requires adding borders to all training images. The method is better described as having a known and controlled intrusion level, which the paper acknowledges by choosing borders over center patterns to minimize impact (Section 5, line 115).

## Nice-to-Haves

- A direct comparison between SolidMark and existing metrics on the *same task*: for a set of training images from the SolidMark-trained model, use standard metrics (e.g., SSCD, modified ℓ₂) to predict whether each image is memorized, and compare precision/recall against SolidMark's border score. This would show whether SolidMark provides genuinely new information beyond what existing metrics capture.
- An analysis of whether images flagged by SolidMark are also memorized in the traditional sense (i.e., whether generations from a generic prompt produce near-identical copies of those training images).
- A simulation or analytical bound for the false positive rate, with a correction (e.g., FDR control) applied to the reported counts.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"SolidMark is an intervention, not a post-hoc evaluation method (structural/fatal)."** Removed because the paper clearly describes the training requirement in Section 4 ("By training the model on these augmented images"), and the method *is* an evaluation method within the setting it defines—it evaluates per-image memorization of the model trained with borders. The paper also releases a pretrained model for use. The framing could be clearer (addressed in Minor weaknesses above), but calling this a "fatal" structural issue is unwarranted given the paper's transparent description of its procedure.

- **"The evaluation only tests recall of training images, not generation of memorized outputs."** Removed because this is a design choice, not a flaw. SolidMark intentionally measures a different kind of memorization signal (the model's ability to recall an embedded key). The paper explicitly notes this as an advantage: it avoids the stochasticity problem of trying to induce a pixel-exact generation. The method is not claiming to replace generation-based metrics but to complement them, as stated in the limitations.

- **"Discontinuity between CIFAR-10 and LAION experiments."** Removed because Section 3's CIFAR-10 experiments are used to analyze *existing* metrics (the ℓ₂ distance analysis from Carlini et al., 2023), not to evaluate SolidMark. The transition to LAION for SolidMark experiments is natural and explained.

- **"Training/evaluation protocol for the border is underspecified."** Removed because Section 4 is reasonably clear: the model is trained on images augmented with borders, and at evaluation time it is prompted to outpaint the border using the training caption. The model has learned during training to handle images with borders; this is a standard fine-tuning setup.

- **"Missing appendix content."** Removed because the parser strips appendix content from all papers; these sections exist in the original submission per the review guidelines.

- **"Absolute numbers not reported in Table 2."** Removed because the table is present in the paper (line 126); parsing artifacts may make it unclear, but the original submission contains the data.

- **Harsh critic's point about "SolidMark is a canary-based detection framework" framing suggestion.** Merged into the Minor weakness about framing, not retained as a separate point.

- **Strength Finder's point about mitigation re-evaluation being a strength.** Demoted because it conflicts with the verified weakness about uncontrolled comparison. The finding is interesting but the evidence is not well-controlled, so it cannot stand as a confidently claimed strength.

## Novel Insights

The harsh critic correctly observes that SolidMark shares conceptual similarities with Needle-in-a-Haystack (NIAH) evaluation for LLMs—both inject a random, unrelated signal into training/serving data and test recall. This connection, which the paper itself draws (Section 2), is worth emphasizing: SolidMark can be seen as a visual-domain analog of NIAH, repurposed from measuring in-context retrieval to measuring training-data memorization. This framing could help bridge the memorization evaluation literature across modalities and suggests a general paradigm for constructing controlled memorization probes. Beyond this observation, the reviews do not surface genuinely novel insights beyond the paper's own contributions.

## Suggestions

1. **Reframe the contribution** in the abstract and introduction: present SolidMark as a *training-time augmentation framework for per-image memorization evaluation* (or a "canary-based detection framework") rather than a general-purpose evaluation metric. This would accurately set expectations and preempt the most common misinterpretation.

2. **Re-run the mitigation experiment (Table 4) with proper controls**: apply both SolidMark and SSCD to the same set of generations from the same model (the border-fine-tuned SD 2.1). This would cleanly isolate whether the discrepancy between metrics is due to the model difference or a genuine difference in what each metric captures.

3. **Quantify the false positive rate**: provide either an analytical bound or simulation results showing the expected number of false memorization reports under the null (no memorization) at each threshold δ. Consider applying an FDR correction to reported counts.

4. **Add confidence intervals** to all experimental tables using bootstrapping or similar resampling methods, especially for the mitigation results in Table 4 where "no meaningful difference" is claimed.
