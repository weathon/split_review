## Human Reviewer 1

### Summary
The paper addresses the problem of evaluating data reliability when ground-truth data are unobserved and only reported data and observations are available. The authors propose a reliability score, the Gram Determinant Score (GDS) defined as the determinant of the Gram matrix of observation distributions, capturing the information diversity among reported data. The paper shows that GDS preserves key reliability orderings and is independent of the observation process. Two estimators are proposed (plug-in and stratified matching), along with a GDS with kernels that generalizes the method to continuous or structured observation spaces.

### Strengths
1.	The paper provides theoretical results on preservation of reliability orderings (Exact, Blackwell, Hamming).
2.	The proposed score admits a geonetrical interpretation.
3.	The GDS with Kernel kernelized extends GDS for application to high-dimensional or structured data (e.g., feature embeddings).

### Weaknesses
1.	The results hold under restrictive assumptions.
2.	Estimation of Gram matrices can be expensive for large $d$ or $N$.
3.	The theoretical strengths of GDS might not easily turn into practical guidance.
4.	Comparaison with other metrics is not provided.

### Questions
1.	The paper does not provide a comparison of the proposed Gram Determinant Score (GDS) with existing reliability metrics. It would be informative to see how GDS performs relative to measures such as mutual information or other established scores.

2.	The computational complexity of the method is not evaluated. In particular, it is unclear whether the kernelized version can scale efficiently to large datasets or high-dimensional embeddings. 

3.	In Experiment 2, the kernel is chosen as $K(y,y’) = \langle y,y’ \rangle$, but the paper does not justify this choice. Could alternative kernels affect the ranking or monotonicity of the score? Are there specific properties a kernel must satisfy for the method to remain valid? Furthermore, which kernel choices are most appropriate for real-world structured data, such as images, text, or signal embeddings?

4.	It is unclear whether the Gram Determinant Score can be normalized across datasets to allow direct comparisons of reliability between heterogeneous datasets. For practical applications, it would also be useful to establish whether a meaningful threshold exists above which a dataset can be considered “reliable.” Clarifying these points would enhance both the interpretability and the practical applicability of the method.

This work makes a conceptually novel and theoretically elegant contribution to the study of data reliability by introducing a unified geometric measure that encompasses several classical reliability orderings. While the theoretical results are compelling and the determinant-based approach is original, the study would benefit from further empirical validation and a more thorough investigation of its scalability and robustness in practical, real-world settings.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
2

---

## Human Reviewer 2

### Summary
The paper introduces a way to score how reliable different reported datasets are. It uses extra signals or observations that are related to the true labels and uses them to tell which dataset is closer to the truth. It formalizes how to say that dataset A is closer to the true data than dataset B, then defines a new score called the Gram Determinant Score to capture that. The score is computed from the joint information between the reported labels and the extra signals, and under some conditions it gives the same ranking no matter which observation process you used. Experiments on synthetic data, CIFAR-10 style image embeddings, and on an employment dataset show that the score goes down when the labels are corrupted, so it can detect which datasets are better and which are noisier.

### Strengths
- The problem is clearly set up. They say what it means for one reported dataset to be better than another and connect it to standard ideas like Blackwell orderings.

- The method has an intuitive picture. Clean data gives a Gram matrix with a bigger determinant. Noisy data makes it smaller.

- The main theorem is strong. If the observation processes are linearly independent, this score gives the same ranking across them and is basically unique.

### Weaknesses
- The strongest results need linearly independent observation processes and some structure on the reporting noise. In real data those conditions may not hold exactly. 

- The score is defined to preserve certain orderings, but in practice you never see those orderings because you never see the true labels. So it can be hard to know if it is right for your case.

- Determinants of Gram matrices can be numerically small and unstable, especially in higher dimensions.

- The experiments are convincing but still mid scale. We do not see behavior for very large label spaces or very heavy class imbalance.

- There is not a wide empirical comparison with other label quality or data pruning methods, so it is hard to tell how big the gain is.

### Questions
- How sensitive is the Gram Determinant Score if the observation process is not perfectly linearly independent but only close to it? Can you show a robustness curve?

- In practice how many samples do we need before the score ranking is stable, especially with many classes?

- How should we pick the kernel and its parameters in the embedding setting?

- Can the score be fooled if a subset of reports is adversarial or all collapsed to a popular class?

- What is the computational cost for large d and can we use low rank or randomized approximations?

- Did you compare to simpler agreement or mutual information based scores on the same datasets?

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
2

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper tackles the novel problem of reliability scoring: assessing dataset quality without ground truth. The authors formalize this setting for data collected from potentially noisy or strategic sources and define several ground-truth–based reliability orderings (Exact Match, Blackwell, Hamming/Distance) as benchmarks for evaluating reliability metrics.

They show fundamental impossibility results, proving that no score can universally preserve all such orderings. To overcome this, the authors propose the Gram Determinant Score (GDS), a geometric measure that quantifies the “volume” spanned by observation distributions — smaller volumes indicate greater deviation from truth. The GDS enjoys strong theoretical properties: it preserves key reliability orderings under mild conditions, is experiment-agnostic (ranking consistency across observation mechanisms), and generalizes naturally to continuous domains via kernelization.

Experiments on synthetic categorical data, CIFAR-10 embeddings, and U.S. employment statistics confirm that the GDS correlates well with ground-truth reliability and consistently ranks more trustworthy datasets higher.

### Strengths
The paper formally introduces the setting of reliability without ground truth, which is both theoretically interesting and practically relevant for data collected from uncertain or biased sources (e.g., social, economic, or self-reported data).

GDS has a clean intuition: it measures the “volume” of observation distributions, which naturally shrinks as the data deviate from truth. This connects statistical structure to an interpretable geometric property.

Experiments cover both synthetic (controlled corruption), vision (CIFAR-10 embeddings), and real-world (employment data) domains, demonstrating the score’s consistency and practical usability.

### Weaknesses
The mathematical framing may be too abstract for practical deployment; real-world users might find the link between Q,P, and reliability difficult to interpret or estimate.

The theoretical results rely on independence and linearity assumptions in the observation model P; it is unclear how robust the score remains when these are violated.

While the three experiments are convincing, all datasets are relatively small-scale or well-structured; results on larger, noisier real-world datasets (e.g., survey or crowd-sourced data) would strengthen claims of generality.

### Questions
Can GDS be intuitively understood as a variance or entropy measure over observation space? How might practitioners interpret a “high” or “low” Gram Determinant Score in practical settings?

In settings where the observation process P is unknown or partially known (e.g., in survey data), how could one practically estimate or approximate P for computing GDS?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
2