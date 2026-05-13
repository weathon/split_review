# SymDiff: Equivariant Diffusion via Stochastic Symmetrisation

- Decision: Accept
- Scores: 8, 8, 5

## Abstract
We propose \symdiff, a novel method for constructing equivariant diffusion models using the recently introduced framework of stochastic symmetrisation.
\symdiff resembles a learned data augmentation that is deployed at sampling time, and is lightweight, computationally efficient, and easy to implement on top of arbitrary off-the-shelf models.
Notably, in contrast to previous work, \symdiff typically does not require any neural network components that are intrinsically equivariant, avoiding the need for complex parameterizations and the use of higher-order geometric features.
Instead, our method can leverage highly scalable modern architectures as drop-in
replacements for these more constrained alternatives.
We show that this additional flexibility yields significant empirical benefit on $\Euclid(3)$-equivariant molecular generation.
To the best of our knowledge, this is the first application of symmetrisation to generative modelling, suggesting its potential in this domain more generally.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new way to build equivariant diffusion models. Whereas traditional methods rely either on simple data augmentation strategies or neural network architectures that are directly constructed to be equivariant, *SymDiff* uses stochastic symmetrization to learn equivariant diffusion models. Stochastic symmetrization is a recently introduced framework by Cornish (2024). On a high level, stochastic symmetrization can intuitively be seen as an advanced data augmentation method, where the augmentation is sampled from an additional, learnable Markov kernel and where the main denoiser network does not need to be equivariant itself. Moreover, the augmentation is also applied during sampling. The paper in detail introduces the approach and rigorously shows that it is principled. SymDiff is then validated on molecule generation, where the permutation equivariance is directly built into the employed networks, whereas rotation equivariance is enforced through stochastic symmetrization. The paper compares to various baselines, showing favourable results, and runs many appropriate and insightful ablation experiments.

### Strengths
**Clarity**: The paper is overall well written and the necessary background is introduced in an appropriate manner, such that one can follow the overall paper. However, the stochastic symmetrization framework is introduced in a fairly abstract manner and I believe more intuitions could be discussed and examples given, which would likely help the broad ICLR audience (see questions below).

**Originality**: Building equivariant diffusion models with stochastic symmetrization is an overall novel and original idea. Methodologically, the approach directly builds on the stochastic symmetrization framework from Cornish (2024). Hence, the novelty here lies in the application of the framework to diffusion models, specifically those for small molecule generation, a popular and important benchmark task.

**Experimental Results**: Overall, the paper is able to show favourable results compared to various baselines, thereby successfully validating the method, and I liked the many ablation experiments that were run.

**Quality and Significance**: Overall, this paper is of high quality and tackles an important problem. Enforcing equivariances and invariances in generative models can be crucial in applications with symmetries, as commonly encountered in scientific applications. However, it is difficult to directly build high-performance and scalable equivariant network architectures. Although quite related to data augmentation methods, stochastic symmetrization and SymDiff proposes a new way to address the problem, and I believe this paper has the potential to result in follow-up work. Hence, I believe this is sufficiently significant for ICLR.

### Weaknesses
I also see some weaknesses.

- *More discussion of intuitions and more experimental analyses*: I think it would be great if the authors discussed some intuitions in more detail and analyzed their models in more detail. Specifically:
  - In practice, training SymDiff boils down to the training procedure in Algorithm 1. $\gamma_\theta$ is trained as part of the ELBO objective, using reparametrization. What sort of $\gamma_\theta$ and $f_\theta$ functions are we intuitively expected to learn in different situations? How does the model intuitively exploit its flexibility to produce more complex $R$ distributions compared to when only using the plain Haar measure? Can examples and intuitions be given?
  - Moreover, is there anything preventing the model from simply learning $R = R_0 f_\theta(...) = I$, this is, no ''augmentation'' at all? In other words, could $f_\theta$ learn to ''undo'' the $R_0$ drawn from the Haar measure so as to remove any rotations? In that case, the training would reduce to standard training without the rotation equivariance, which may be beneficial from the objective's perspective considering that the network itself isn't equivariant? But this defeats the purpose of the method. Such potential edge cases should be discussed.
  - To this end, can the authors maybe show and analyze what sort of $\gamma_\theta$ distributions SymDiff ends up learning in practice?
  - The approach uses $\gamma_\theta$ (or $f_\theta$) also during sampling. What is the intuition for that? And what would happen if we didn't apply $\gamma_\theta$ during sampling? This would be an interesting discussion or ablation. Moreover, in the case without learnable $\gamma_\theta$, i.e. when using only the Haar measure, I would expect that the model would still perform fine even if no $R$ is applied during sampling.

- *Relation to data augmentation*: Related to the last point above, overall, it seems that SymDiff can be seen as a sophisticated data augmentation strategy (as also pointed out by the authors). However, the authors carefully distinguish the case between training with data augmentation (DiT-Aug) and SymDiff with Haar measure sampling only (SymDiff-H), pointing out that the only difference in that case is that SymDiff-H also applies augmentations during sampling, if I understood things correctly. However, in all experiments the performance of DiT-Aug and SymDiff-H is extremely close together. This makes me believe the application of the augmentation during sampling isn't necessary for SymDiff-H (also see point above), and that SymDiff-H really just corresponds to standard data augmentation. Related to that, it is not sufficiently well discussed, explained and analyzed how exactly this situation *qualitatively* changes when $\gamma_\theta$ is learnt (see point above).

- *Experimental results*: The performance gains over the EDM baseline are meaningfully large, but at the same time compared to more sophisticated baseline models SymDiff does not perform much better. Further, the authors make the point that the comparison to EDM is fair. However, the very different network sizes still make a fair comparison somewhat difficult. How would performance between EDM and SymDiff compare for similar-sized neural networks?

**Conclusion:** SymDiff is an interesting and novel method, tackling a significant problem, and I believe it is of interest to the ICLR audience. However, there are various fundamental questions about the method and the experiments (see above), that I hope the authors can answer and address. For now, I am leaning towards suggesting acceptance.

### Questions
I have put almost all my questions in the ''Weaknesses'' section above already, but I have one very minor additional question. In 4.2, the authors write that, given the size of GEOM-Drugs, they train a smaller model than on QM9. But the GEOM-Drugs dataset is larger and more complex than QM9. Wouldn't one want to train a larger, more expressive model in that case, and not a smaller one?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper “SymDiff: Equivariant Diffusion via Stochastic Symmetrisation” introduces SYMDIFF, a novel method for constructing equivariant diffusion models without the need for complex, intrinsically equivariant neural networks. Traditional approaches often rely on specialized architectures with complex parameterizations and higher-order geometric features to achieve equivariance, which can be computationally intensive and challenging to implement.

SYMDIFF leverages the framework of stochastic symmetrisation, effectively functioning as a learned data augmentation technique applied during the sampling phase. This approach is lightweight, computationally efficient, and can be easily implemented on top of arbitrary off-the-shelf models. By not requiring the neural network components to be intrinsically equivariant, SYMDIFF allows the use of highly scalable modern architectures, providing greater flexibility and performance.

The authors demonstrate the effectiveness and scalability of SYMDIFF through empirical experiments on E(3)-equivariant molecular generation tasks using the well-known QM9 and GEOM-DRUGS datasets. The results show significant improvements over traditional methods, highlighting the benefits of SYMDIFF in generating molecular structures that are equivariant under the E(3) group (which includes translations, rotations, and reflections in three-dimensional space).

This work represents the first application of stochastic symmetrisation to generative modeling, suggesting that SYMDIFF has the potential for broader applications in the domain of equivariant machine learning models.

### Strengths
This paper introduces SYMDIFF, a simple yet powerful method for constructing equivariant diffusion models without relying on complex intrinsically equivariant neural network architectures. The strengths of the paper can be assessed across the following dimensions:

Originality:
The paper presents a novel application of stochastic symmetrisation to generative modeling, specifically in the context of diffusion models. This approach is original because it departs from traditional methods that require specialized equivariant architectures with complex parameterizations and higher-order geometric features. By leveraging stochastic symmetrisation as a learned data augmentation technique applied during sampling, the paper creatively combines existing ideas to overcome limitations of prior models. This opens up new possibilities for using standard neural network architectures in equivariant settings.

Quality:
The paper demonstrates high quality in both theoretical and empirical aspects. It provides a solid theoretical foundation based on Markov kernels, offering a clear understanding of how SYMDIFF achieves equivariance without specialized architectures. The empirical evaluations are thorough, showcasing the method’s effectiveness on E(3)-equivariant molecular generation tasks using the well-known QM9 and GEOM-DRUGS datasets. The results indicate significant performance improvements and scalability advantages over traditional equivariant models. The experiments are well-designed, and the conclusions are well-supported by the data.

Clarity:
The paper is written with clarity and precision, making complex concepts accessible to the reader. It systematically introduces the theoretical background before delving into the methodological details of SYMDIFF. The explanations are clear, and algorithmic descriptions helps in understanding the implementation. The empirical results are presented in an organized manner, with insightful discussions that highlight the implications of the findings. Overall, the paper effectively communicates its contributions and significance.

Significance:
The significance of the paper lies in its potential to impact the field of equivariant machine learning models substantially. By eliminating the need for specialized equivariant architectures, SYMDIFF lowers the barrier to entry for researchers and practitioners interested in building equivariant models. It enables the use of arbitrary off-the-shelf neural network architectures, which are often more scalable and easier to implement. This flexibility can accelerate the development and deployment of equivariant models in various applications, including molecular generation, computer vision, and physics-based simulations. Moreover, being the first to apply stochastic symmetrisation to generative modeling, the paper paves the way for future research in this promising direction.

### Weaknesses
While the paper introduces SYMDIFF as a flexible and efficient method for constructing equivariant diffusion models, it lacks specific guidelines to help practitioners decide when to use SYMDIFF over traditional intrinsically equivariant models. This absence of decision-making support makes it challenging to understand the circumstances under which SYMDIFF is more advantageous.

To address this, I suggest the authors include a comparative analysis between SYMDIFF and traditional methods. This could be presented as a table or flowchart highlighting key factors such as:

- Dataset Characteristics: Situations where SYMDIFF performs better or worse.
- Model Complexity: Differences in architecture and scalability.
- Computational Resources: Comparisons of memory usage, training time, and inference speed.
- Performance Metrics: Quantitative comparisons on accuracy and sample quality.
- Ease of Implementation: Practical considerations like code complexity.

Including such a comparison would provide clear guidance for practitioners, making the paper more actionable and useful.

Additionally, while the paper claims that SYMDIFF is computationally efficient, it doesn’t provide empirical evidence to support this. I recommend the authors include:

- Empirical Benchmarks: Runtime analysis and resource consumption statistics compared to intrinsically equivariant models.
- Convergence Plots: Performance versus number of training epochs for both SYMDIFF and baseline methods.
- Ablation Studies: Impact of stochastic symmetrisation on computational overhead and model performance.

By incorporating these elements, the paper would strengthen its claims and offer actionable insights, enabling readers to make informed decisions about adopting SYMDIFF.

### Questions
- Do you have insights into how many training epochs are necessary for SYMDIFF to effectively learn equivariance in the molecular generation task?
- How does the convergence speed of SYMDIFF compare to that of intrinsically equivariant models in learning equivariant properties?
- In the context of molecular generation, do you consider the equivariant component of the task to be a minor or major challenge compared to learning the underlying chemical laws necessary for accurate atom placement?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes SymDiff, a novel method for constructing equivariant diffusion models via stochastic symmetrisation. It addresses limitations of prior work on geometric data by allowing more flexibility than using intrinsically equivariant neural networks. Experiments on QM9 and GEOM-Drugs datasets for molecular generation show SymDiff outperforms EDM and is competitive with other baselines, with better scalability. SymDiff can be seen as a generalisation of data augmentation, with a learned and deployed augmentation process ensuring stochastic equivariance.

### Strengths
- Originality: The paper proposes SymDiff, a novel method using stochastic symmetrisation for equivariant diffusion models, extending symmetrisation to generative modelling and differing from prior approaches.

- Clarity: The paper is well-structured, clearly explaining concepts with examples and presenting algorithms, aiding understanding and implementation.

- Quality: The paper presents a comprehensive framework with solid derivations and conducts rigorous experiments on multiple datasets.

### Weaknesses
- Performance gap: from Tab2 and 3, seems the model is not parameter efficient compared with baseline models. When reducing the model size, the performance will have a larger drop than the baseline model.

- Unfair comparison: I didn't fully understand for SymDiff+++, ++, and +, why you cannot choose the same number of parameters of EDM. It seems your model SymDiff+ is already larger than EDM+++, but with worse performance.

- Missing comparison: I think the author also needs to incorporate GeoLDM with different sizes into Tab 2 and 3, which potentially can work better since it acts on low-dimensional space.

### Questions
- Why SymDiff require larger model size to match the performance of EDM / GeoLDM etc.

### Soundness
3

### Presentation
3

### Contribution
3
