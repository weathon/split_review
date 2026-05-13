# The Rate-Distortion-Perception Trade-Off with Algorithmic Realism

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Realism constraints (or constraints on perceptual quality) have received considerable recent attention within the context of lossy compression, particularly of images. Theoretical studies of lossy compression indicate that high-rate common randomness between the compressor and the decompressor is a valuable resource for achieving realism. On the other hand, the utility of significant amounts of common randomness at test time has not been noted in practice. We offer an explanation for this discrepancy by considering a realism constraint that requires satisfying a universal critic that inspects realizations of individual compressed images, or batches thereof. We characterize the optimal rate-distortion-perception trade-off under such a realism constraint, and show that it is asymptotically achievable without any common randomness, unless the batch size is impractically large.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper concerns with the rate-distortion-perception tradeoff (RDP) in the context of lossy compression and argues that previous theoretical results, which suggest that common randomness between the encoder and the decoder is crucial for good performance, do not accurately reflect how humans perceive realism. To address this, the authors reformulate the RDP with reaslim constraints by adopting the concept of universal critic that generalizes no-reference metrics and divergences and insecpt batches of samples. Under this framework, they prove that near-perfect realism is achievable without common randomness unless the batch size is impractically large and the proposed realism measure reduces to a divergence.

### Strengths
* The paper provides a novel perspective on the rate-distortion-perception tradeoff by adopting the concept of universal critics.
* The paper presents rigorous theoretical analysis and proofs to support its claims.
* The theoretical finding that near-perfect realism is achievable without common randomness has significant practical implications for lossy compression.

### Weaknesses
While the paper presents a novel and potentially impactful contribution, its clarity and accessibility are hindered by a dense presentation style. The heavy use of technical notation and the lack of illustrative examples make it challenging to grasp the core concepts and implications of the proposed framework.

Specifically, the paper would benefit from:

* More explanatory discussions: For instance, a concise discussion following Definition 3.3 would clarify the meaning and significance of the new formulation in comparison to the original RDP framework.

* Illustrative examples: Simple case studies or visual examples would help readers understand the practical implications of the theoretical results. The authors could consider drawing inspiration from the original RDP paper by Blau & Michaeli, which effectively uses examples to convey its ideas.

Addressing these issues would make the paper more accessible to a wider audience and increase its impact. While the core contribution merits acceptance, I strongly encourage the authors to revise the paper with a focus on clarity and illustrative examples.

### Questions
1. Does common randomness offer any benefits beyond perceptual realism in lossy compression? For example, stability/robustness? 
2. How does the achievable rate-distortion-perception tradeoff change as a function of the batch size used by the universal critic?  Does this analysis offer any insights into selecting an appropriate batch size for training generative compression models that aim to satisfy perceptual quality constraints?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The study addresses a core issue in lossy image compression: achieving high perceptual quality in the decompressed images while minimizing distortion and compression rate. A unique aspect of this paper is its focus on algorithmic realism — a concept that considers human perception and aims to create compressed images that appear realistic to a critic. This builds on prior work on the rate-distortion-perception (RDP) trade-off, but instead of relying heavily on common randomness, it introduces a framework that reduces or eliminates the need for shared randomness between encoder and decoder in practical settings.

### Strengths
1. Interesting Insight into Realism Constraints: By redefining perceptual realism through an algorithmic lens, the paper provides a fresh perspective on the RDP trade-off and its practical applications in lossy compression.
2. Reduced Dependency on Common Randomness: The finding that common randomness is only needed in impractically large batches addresses a significant gap in previous theoretical predictions versus experimental observations.
3. Good Theoretical Foundation: The study provides rigorous proof and aligns well with information theory, making it a valuable resource for researchers interested in theoretical advances in compression.

### Weaknesses
While the paper provides rigorous theoretical derivations and proofs, one significant limitation is the lack of practical illustrations or implementations that could help readers appreciate the impact and contributions of the proposed framework in real-world applications. The authors claim that algorithmic realism simplifies the practical attainment of the rate-distortion-perception (RDP) trade-off by reducing the dependency on common randomness between encoder and decoder. However, without practical visualizations or demonstration attempts, it becomes challenging for readers to intuitively evaluate the work’s contributions.

Though I acknowledge the value of theoretical derivations, the paper appears incomplete and, consequently, less persuasive without empirical validation. I strongly recommend that the authors complement their theoretical results with practical experiments, such as specific implementations, visual examples, or a demonstration. This would significantly enhance the paper’s credibility and provide readers with a tangible understanding of the theory’s implications.

To make these points more specific, I propose the following questions:

 **1. Evaluation of Practical Applicability**

The paper offers extensive theoretical proofs, yet there is no concrete implementation provided to demonstrate how this framework could be integrated into real-world image compression tasks. Could the authors consider validating the proposed approach on an actual compression system to illustrate its practical efficacy?

 **2. Feasibility of Reducing Common Randomness.**

While the theory is sound, it would benefit from an empirical investigation to verify that reducing common randomness does not detract from visual quality. Without experimental validation, how can readers assess the applicability of these theoretical findings to practical compression systems?

   **3. Experimental Support for Theory-Practice Connection**

 The paper’s theoretical framework is detailed but lacks experimental applications or use cases. Could the authors consider providing experiments to demonstrate the balance of visual quality and compression rate achieved by the proposed approach?

   **4. Inclusion of Visual Case Studies**

 Given the claims of practical feasibility, is it possible to provide specific examples of compressed and decompressed images to offer readers a more direct perception of the quality improvement achieved by the proposed approach?

These additions would substantially enhance the paper by bridging the gap between theoretical results and their practical impact, allowing readers to more fully appreciate the contributions of this work.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper propose a new rate-distortion-perception function and proves its achievabiliy and converse, in both zero-shot and asymptotical setting. The proposed RDP function replace the P from divergence to a realism measure defined by authors. The propose RDP function is achievable without common randomness.

### Strengths
It is great to have a RDP which is achievable without randomness. Afterall, the human eye distinguishs images in a per-image setting without randomness. The proposed RDP is better aligned to human perception in this sense. I have not went through the details of proofs due to the complex notation. However, I am in general glad to see a new RDP function with achievability & converse, zero-shot & asymptotic.

### Weaknesses
The reason why I am not willing to give this paper a higher rating is that the authors have not shown how the proposed RDP can guide perceptual compression / super-resolution, not even a toy example.

The RDP function in [Blau & Michaeli 2019] has many disadvantages, which this paper does not have:
* [Blau & Michaeli 2019] does not prove the converse.
* [Blau & Michaeli 2019] does not distinguish zero-shot and asymptotic function.
Those issues have not been fixed until [A coding theorem for the rate-distortion-perception function].

However, those weakness does not stop [Blau & Michaeli 2019] being popular. This is because [Blau & Michaeli 2019] has clear application in perceptual compression / super-resolution. It explains why previous work using GAN for perceptual compression; It aligns very well with the practically used "real vs. fake" test; It even guides later works in diffusion based image compression.

ICLR is a machine learning venue, not a pure information theory venue such as ISIT / TIT. It is better to have numerical examples (even toy size) and suggestions for later application works, so that the later works in ICLR can benefits from this paper more.

(minor) It is better to move the converse to the main paper, as this year we have 10 page budget. It is strange to have a 8 page paper and 20 page appendix. At least for me, the converse is as important as achievability.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new mathematical formulation for the rate-perception-distortion tradeoff. Specifically, in the previous rate-perception-distortion formulation, the perceptual quality constraint is a constraint on the statistical divergence between the distribution of the decoded images and that of the clean images. In theory, this typically leads to randomized decoders, which produce many different decoded images given an encoded one. However, in practice, high-perceptual-quality compression-decompression algorithms rarely incorporate such randomness.
To explain this phenomenon, the authors replace the perceptual quality constraint with a new interesting concept called the "universal critic", which poses a perceptual quality constraint on individual images (or on a batch of images).
The new rate-perception-distortion formulation leads to solutions which do not incorporate randomness. This is a sensible result given the fact that now there is no constraint on the *distribution* of the decoded images.

### Strengths
This paper is incredibly interesting, and written very well. The theoretical results are interesting and serve a highly important contribution to the community of information theorists.

### Weaknesses
1. There are no experiments, demonstrations, simulations, presented evidence, etc. This paper contains only theoretical results, which is not necessarily a bad thing, but I am not sure whether it's a fit for the ICLR community (most of which are practitioners). I would expect to see this paper in a theoretical journal.

2. There is no discussion/limitation section discussing the possible future continuation of this work.

### Questions
1. I am aware that universal critics cannot be implemented practically, but still, is there a way to somehow simulate/demonstrate the new tradeoff on simple examples (perhaps a Bernoulli source)?

2. Is there a way to demonstrate on previous works that less randomness is indeed attributed to better universal critic scores? Namely, is it possible to demonstrate that one may benefit from better rate&distortion by avoiding randomness, but still achieving high-perceptual-quality in the sense of universal critics?

### Soundness
2

### Presentation
3

### Contribution
4
