## Summary

This paper conducts an empirical study of encoder and decoder architectural choices in Variational Autoencoders (VAEs). It systematically varies combinations of dense networks (DNNs) and convolutional networks (CNNs) for encoders and decoders on MNIST, across different latent space sizes, and evaluates reconstruction loss, generative (KLD-based) loss, and latent space structure via PCA. The main claims are: (1) small dense encoders generally outperform deeper or convolutional ones; (2) multi-block CNN decoders are preferable for decoding; (3) non-zero KLD loss is beneficial; (4) high compression degrades latent space quality.

---

## Strengths

- **Legitimate research question**: Investigating the effect of encoder/decoder architecture on VAE behavior is a meaningful direction—it is underexplored relative to the volume of work on loss functions and priors.
- **Systematic design**: The paper attempts a structured combinatorial search over encoder/decoder types and latent space sizes, producing a non-trivial number of experimental conditions.

---

## Weaknesses

### Fatal

1. **Single, trivially simple dataset (MNIST)**: All experiments are conducted exclusively on MNIST, a dataset so well-understood that conclusions drawn from it have virtually no generalizing power to real-world VAE design. For an architecture study to be actionable, findings must hold across multiple datasets of varying complexity (e.g., CIFAR-10, CelebA). Claiming architectural principles from MNIST alone is methodologically indefensible.

2. **No standard generative modeling evaluation metrics**: The paper evaluates generation quality using only reconstruction loss (BCE) and KLD-based loss. Standard metrics like FID or IS—which are essential for validating generation quality claims—are entirely absent. The paper therefore cannot substantiate claims about "generative quality."

3. **Critical experimental details are missing**: There is no description of the optimizer, learning rate, batch size, number of epochs, β weighting of KLD, or number of runs per configuration. Without this information, the results are irreproducible.

4. **Non-standard and potentially erroneous loss terminology**: The y-axis of Figure 1 is labeled "ReLU divergence loss," which is not a recognized term in the VAE literature. The ELBO involves KLD and reconstruction loss; the use of a non-standard term without definition raises concern about the correctness of the training objective. Similarly, the KLD values in Figure 2 (ranging from −22 to −18 on a log scale) indicate near-total posterior collapse in the "top 25%" models—yet these are presented as the best performers, which is contradictory.

### Major

5. **Findings are largely well-known or trivially expected**: That posterior collapse (KLD≈0) is harmful is standard knowledge, as is the fact that CNNs are well-suited for spatially structured (image) decoding while compact encoders risk less information bottleneck. The NVAE paper, which the authors themselves cite, already emphasizes architectural asymmetry in VAEs. The paper does not situate how its findings extend, refine, or contradict prior work.

6. **Methodologically unsound "top 25%" selection**: The paper repeatedly restricts analysis to the "top 25%" (or 50%) of models by one metric, then draws architectural conclusions from the counts in that subset. The total number of configurations evaluated is never clearly stated, making these counts uninterpretable. With 5–11 models per architecture type in the top subset (Figure 4), the differences are not tested for statistical significance.

7. **No error bars or statistical tests**: Every numerical comparison in the paper is presented without any measure of variance (across seeds), making it impossible to determine whether observed differences are meaningful.

### Minor

8. **The BCE values in Figure 2 (0.00000–0.00020) appear abnormally small for per-pixel MNIST reconstruction**, suggesting either per-pixel scaling or normalization inconsistency that is never explained.

9. **PCA of 2D projections as the sole latent space evaluation**: No disentanglement metrics, mutual information estimates, or sample quality visualizations are included, limiting the analysis of latent space structure.

### Trivial

- The label grammar used in figures (e.g., `L{latent size}.{Encode arch}{num layers}.{Decoder arch}{num layers}`) is inconsistent across figures.

---

## Nice-to-Haves

- Reproducing the study on CelebA, CIFAR-10, or a structured dataset would substantially strengthen the claims.
- Including β-VAE variants and ablating β alongside architecture would disentangle the role of regularization from architecture.
- Reporting FID/IS alongside ELBO components would make comparisons meaningful.

---

## Novel Insights

None beyond the paper's own contributions. The findings are either consistent with established results (posterior collapse is bad; CNNs excel at image decoding) or too narrowly grounded in a single dataset to constitute generalizable insight. The asymmetry between simple encoders and complex decoders aligns directly with what NVAE and related work have already documented.

---

## Suggestions

- Expand experiments to at least two non-trivial datasets (e.g., CIFAR-10 and CelebA) to check whether architectural conclusions hold beyond MNIST.
- Define and justify the training objective precisely; the "ReLU divergence loss" label must be replaced with a mathematically precise formulation.
- Report mean ± standard deviation over at least 3 random seeds for every configuration.
- Use FID or IS to complement reconstruction/KLD-based evaluation.
- Conduct proper statistical tests (e.g., Wilcoxon rank-sum or bootstrap tests) when comparing architectural groups.

---

## Score and Decision

The paper addresses a real question but is fundamentally undermined by single-dataset scope on MNIST, non-standard and potentially incorrect loss formulations, missing hyperparameter details, no standard generative metrics, and findings that are substantially consistent with existing knowledge. These are not minor polish issues—they jointly prevent any confident conclusion from being drawn. The work, as presented, does not meet the rigor expected at ICLR.

MY FINAL SCORE: <score>1</score>
MY FINAL DECISION: <decision>Reject</decision>