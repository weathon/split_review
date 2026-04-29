# Position: Significant impact of numerical precision in scientific machine learning

- Decision: Reject
- Scores: 4, 7, 3

## Abstract
The machine learning community has focused on computational efficiency, often leveraging lower-precision formats such as FP16, instead of the standard FP32.
In contrast, little attention has been paid to higher-precision formats, such as FP64, despite their critical role in scientific domains like materials science, where even small numerical differences can lead to significant inaccuracies in physicochemical properties.
This need for high precision extends to the emerging field of \textit{machine learning for scientific tasks}, yet it has not been thoroughly investigated.
According to several studies and our toy experiment, models trained with FP32 show insufficient accuracy compared to those trained with FP64, indicating that higher precision is also crucial in scientific machine learning, as in traditional scientific computing.
This precision issue limits the potential of scientific machine learning that can replace the traditional scientific computings in practical research.
Our position paper not only highlights these precision-related issues but also recommends reporting comparisons between FP32 and FP64 results, encouraging the release of FP64 models.
We believe that these efforts can enable machine learning to contribute meaningfully to the natural sciences, ensuring both scientific reliability and practical applicability.

## Human Reviews

## Human Reviewer 1

### Rating
4

### Rating Number
4

### Confidence
4

### Summary
The paper argues that numeric precision is a critical aspect of scientific computing, and therefore should be a more explicit focus of attention in scientific machine learning. The paper discusses examples from learned potentials, physics informed neural nets, and the use of llm-based models in science. The paper calls for a rigorous study of the impact of numeric precision on the accuracy of ML models used in various scientific applications.

### Strengths
The paper tries to bridge gaps between requirements in the scientific computing community and the ML community and broaden the dialogue around the differing requirements of scientific computing. The paper gives concrete examples of scientific computing methods that are impacted by numeric precision issues. A good case is made that in certain cases, numeric issues can lead to poor performances in scientific applications, and the paper provides a clear call for action for studying the phenomenon more closely.

### Weaknesses
The paper does not provide strong evidence that numeric precision is an issue in any of the three areas that are investigated. In particular, for section 3.1, the mismatch between the 32bit and 64bit models does not necessarily indicate that the 64bit model is more accurate.

While precision might impact accuracy, it does not seem fundamentally different than any of the other hyper-parameter that need to be adjusted to obtain good performance, such as learning rate, weight decay, architecture choices etc. If there is a qualitative difference, that should be made more clear in the paper.

There is also not a strong argument about what can be gained from a systematic review. A thorough review will likely yield the answer of "it depends". It might be possible to specify in which cases precision is critical (such as in the case mentioned in 3.2), which would be useful for practitioners. However, this would be a case of "beneficial guidance" more than "significant impact".

### Questions
Can you elaborate on how precision issues in scientific ML are closely tied to ethical concerns regarting the reliability of the findings? Generally, accuracy of ML methods is only statistical in nature, and is measured usually (in supervised learning) using a hold-out test-set. This measurement of reliability is unrelated to the precision or reliability of the model. The reliability of any model can usually only be assessed in this way.

In Q2, you mention "observed inaccuracies". Can you be more specific in what you mean by that? Also, are you attributing inaccuracies to precision issues? It is quite rate that inaccuracies of a model can be directly attributed to any particular aspect of a model.

### Presentation
2

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This paper argues that numerical precision (FP64) is critical in scientific machine learning (ML), highlighting how insufficient precision (FP32) can significantly degrade outcomes. The authors advocate for systematic benchmarking of FP32 vs. FP64, encouraging the community to report and release FP64-trained models.

### Strengths
The paper clearly argues for the importance of numerical precision in scientific ML, supported by detailed and relevant examples from various scientific fields. Recommendations for systematic benchmarking and public release of FP64 models are actionable and likely to be impactful. Alternative viewpoints are thoroughly addressed, enhancing the robustness of the paper.

### Weaknesses
The discussion could benefit from a more detailed quantitative analysis of the computational overhead associated with FP64. Additional empirical evidence specifically from ML experiments would strengthen the argument further. Exploration of mixed-precision strategies is mentioned but could benefit from deeper technical elaboration.

### Questions
Could the authors provide preliminary data or further insights into the computational overhead involved in using mixed FP32-FP64 precision?

Have the authors identified scenarios where FP32 is sufficient, and could they elaborate on criteria that distinguish these scenarios from FP64-sensitive tasks?

### Presentation
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The papers argues that the precision of computations should be increased in the hope that more accurate results will be produced.

### Strengths
The authors are absolutely right (lines 4-6) that in "materials science, where even small numerical differences can lead to significant inaccuracies in physicochemical properties". 

The much worse overlooked problem is the discontinuity of cell-based representations of periodic materials, because almost any perturbation of atoms can arbitrarily scale up a primitive (or reduced) cell, which has been know experimentally since 1965 (Lawton, Stephen L., and Robert A. Jacobson. The reduced cell and its crystallographic applications. No. IS-1141. Ames Lab., Iowa State Univ. of Science and Tech., US) and comparisons by unit cells (or motifs) unreliable as well as materials databases using unstable cells.  

Figure 1 gives a crucial counter-example to the DFT outputting physically unrealistic molecules of water. The included example does not prove that the DFT is correct at any (lower or higher) precision except that this single example seems correct. In general, examples prove nothing, while counter-examples disprove conjectures, so Figure 1 has disproved the conjecture that the DFT can be used in practice.

### Weaknesses
Responding to "This need for high precision extends to the emerging field of machine learning for scientific tasks, yet it has not been thoroughly investigated" (lines 6-7), the precision have been thoroughly investigated by mathematicians and other scientists, which has led to the development of chaos theory discovered by Edward Lorenz using computers, so computer scientists should learn this.

Increasing precision is worthless because any real (not too simple) dynamical system unpredictably changes its behavior under tiny perturbations of initial conditions or parameters. This "butterfly effect" emerges even for 1-variable maps: x->4x(1-x), where perturbing any initial x in [0,1] produces a random sequence. 

The chaos theory was honored by the 1977 Nobel Prize in Chemistry to Ilya Prigogin but seems to be completely forgotten in favor of artificial illusions consuming more and more resources by promising to quantify uncertainties that should be embraced in the real world.

### Questions
Can the authors list machine learning algorithms that are guaranteed to produce stable results, e.g. Lipschitz continuous under perturbations? Such a list would provide a good incentive not to waste time and resources on impractical approaches, which endanger the life on Earth, at least through increased emissions of greenhouse gases.

### Presentation
2
