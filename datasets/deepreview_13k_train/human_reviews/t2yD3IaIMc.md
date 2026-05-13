# Hypernetwork-Based Equivariant CNNs

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
In geometric deep learning, numerous works have been dedicated to enhancing neural networks with ability to preserve symmetries, a concept known as equivariance. Convolutional Neural Networks (CNNs) are already equivariant to translations. To further achieve rotation and reflection equivariance, previous methods are primarily based on Group Equivariant Convolutional Neural Networks ($G$-CNN). While showing a significant improvement when processing rotation-augmented datasets, training $G$-CNN on a dataset with little rotational variation typically leads to a performance drop comparing to a regular CNN. In this study, we discuss the reason of $G$-CNN not performing on datasets with little rotational variation. We propose an alternative approach: generating CNN filters that inherently exhibit rotational equivariance without altering the main network's CNN structure. This is achieved through our novel application of a dynamic hypernetwork. We prove these generated filters grant equivariance property to a regular CNN main network. Our experiments demonstrate that our method outperforms $G$-CNN and achieves performance comparable to advanced state-of-the-art $G$-CNN-based methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes using hypernetworks to generate convolutional filters and coefficients based on rotated inputs. These filters are then applied in a convolutional layer, while the coefficients are used in a subsequent linear layer, enabling translation-rotation equivariance. Compared to the first G-CNN, the proposed method achieves higher accuracy, demonstrating its effectiveness even with minimal rotational variation.

### Strengths
The idea of using hypernetwork to achieve rotation equivariant filters and coefficients is interesting.

### Weaknesses
1. Outdated and Inconsistent Baselines: The proposed method is shown to perform better than the original G-CNN by Cohen & Welling (2016). However, recent advances in steerable G-CNNs already address rotational variation effectively. While this paper includes steerable G-CNN results for the rotated MNIST experiment, none are tested in the CIFAR-10/100 experiments. Additionally, the proposed method underperforms compared to E2CNN, a steerable G-CNN, raising questions about the strength of this baseline comparison. Given more advanced methods are available, outperforming only the original G-CNN is not sufficiently convincing. Moreover, the steerable G-CNN has a nice theoretical explanation, which is related to Nyquist–Shannon sampling theorem, whereas the proposed method is empirical.
2. Missing Parameter Counts: Matching the number of network parameters is crucial to ensure that performance gains are not simply due to an increase in parameters. Parameter counts are absent, making it difficult to assess the efficiency of the proposed method.
3. Questionable Results in Table 3: The results in Table 3 lack thorough discussion and seem questionable. P4-CNN and Z4-HE-CNN exhibit similar translation-rotation group equivariance on rotated MNIST. Assuming they have similar parameter counts, this could indicate that the proposed hypernetwork-based method may improve over equivariance-based methods for minimal rotational variation. However, models like LieConv, Steerable-CNN, E2FCNN, and Sim2-CNN are designed for continuous rotation and show optimal results with 16 orientation samples, yet they perform worse than the proposed Z4-HE-CNN. The results of Z4-HE-CNN (LoRA) appear more reasonable than Z4-HE-CNN. Without matched number of parameters, the state-of-the-art claim is questionable.

4. Limited Generalizability to Other Transformations: The use of hard-coded 90-degree rotations (Figure 2) and specific permutations (Figure 3) may limit generalizability to transformations like scaling and shear. Although 90-degree rotations avoid interpolation issues, this discrete approach could face challenges when applied to continuous transformations, such as scaling and shear.

5. Issues with Filter Generation from Rotated Inputs: Generating convolutional filters from rotated input images could present a problem. Since the translation-rotation group does not commute (i.e., rotation followed by translation differs from translation followed by rotation), G-CNNs typically rotate the convolutional filters rather than the input images. While the proposed method achieves translation-rotation equivariance, the approach of generating filters based on rotated inputs could introduce inconsistencies, as translation of the input image would alter the generated filters. Fortunately, the use of a regular CNN as the NEP helps maintain some robustness to translation. However, standard CNNs face challenges in achieving ideal translation equivariance [1]. While this paper focuses on rotation equivariance, neglecting translation equivariance could impact the proposed method more significantly than in other G-CNNs.

### Questions
1. What is the train/test split for the MNIST datasets used in this paper? Is it 12k/50k?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work presents HE-CNNs. An equivariant neural architecture method, where the network parameters are generated based on a hypernetwork in a way that it is equivariant to a defined (finite & small) group. The authors compare their method to G-CNNs and demonstrate competitive results with regard to existing state-of-the-art (although relatively old) methods.

### Strengths
- To the best of my knowledge, the way proposed in this paper to construct equivariant filters is novel. I’ve not seen such an approach before.

### Weaknesses
While the method proposed in this paper is new, I have concerns along several different axes: scalability, the conclusions drawn, and the analysis of why the method works.

- My most important concern is that the scalability of the method is really problematic. This touches upon compute efficiency, large networks, large batches, large groups, etc. Note that some of these issues are not even mentioned in the paper. The paper lacks an explicit limitations section as well, where all of these scaling issues should be clearly stated.

  - First, in terms of computation, this method basically uses a neural network to generate the weights of another neural network. Consequently, one could argue that this imposes important constraints on the size that the hypernetwork may have. Unfortunately, the authors do not touch upon runtime etc compared to non-hypernetwork-based networks.
  - Next, the method requires passing N versions of the input through the network –where N is the size of the group– for every single input in an input batch, in order to generate equivariant weights. This becomes a clear constraint for large –let alone continuous– groups. The authors also do not mention this.
  - Then, the hypernetwork must generate weights for the whole of the other network. This is another important scalability constraint over the size of the hypernetwork required in those settings. It also calls into question how big that network needs to become for growing sizes of the main network. The authors use LoRA to this end, but in my view this does not solve the scalability issues of the method.
  - Next, the authors mention that the method is equivariant only if all inputs in a single batch have the same orientation. This is, of course, very unrealistic and in my view an extremely constraining limitation. As an alternative, one can generate different network weights for each one input, but this, again, does not scale.

- Aside from the scalability issue, I am also concerned about the last point mentioned above. From what I understand, the method assumes that it is known what g transformation is applied to the input. Note that, if this were the case in realistic settings, this would dramatically simplify how equivariant methods work. 

- Next, the authors argue that the reason HE-CNNs work better than baseline G-CNNs is the fact that the kernels in G-CNNs are constrained. However, I am inclined to believe that there are, in fact, two composing factors leading to better results. Note that, in contrast to G-CNNs, the weights of HE-CNNs are input dependent. Yet, there is no analysis on whether the gains result from not constraining kernels in the main input, or from this input dependency. I emphasize that lack of this analysis may be leading to incorrect conclusions. For instance, it could be completely possible that the gains are not from constraining the kernels, but in fact because these kernels are input dependent. I encourage the authors to include such analyses.

### Questions
* Is it correct that the method assumes that the orientation of the input is know beforehand? If not, how is it that  the $a_r^i$ can be described relative to a canonical direction? 

### Limitations

The authors do not state clearly the limitations of their method. There is no specific section dedicated to this.

### Conclusion

While I believe that the method proposed here is novel, I have several concerns about the method proposed, its inner working and its use in practice. I believe there is potential, but, in my view, the method, the paper and the experimental analysis must be polished before this paper can be accepted. I am therefore, unable to support acceptance at this point.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Hypernetwork-based Equivariant CNNs (HE-CNN), a hypernetwork-based approach to achieve rotational equivariance in convolutional neural networks. Unlike Group Equivariant CNNs (G-CNNs) that impose a filter constraint, HE-CNN uses a dynamic hypernetwork to generate input-dependent parameters that inherently exhibit equivariance. The hypernetwork consists of a non-equivariant parameter-pieces generator and an equivariant combiner that assembles the pieces to form equivariant parameters. The authors provide theoretical proofs of the model's equivariance properties and demonstrate its effectiveness through experiments on multiple benchmark datasets including MNIST, CIFAR10/100, and STL10. HE-CNN demonstrates comparable performance on those datasets.

### Strengths
- The authors propose to directly utilize the dynamic hypernetwork to generate equivariant parameters.
- The proposed design of using hypernetwork for equivariance is validated in small-scale experiments.

### Weaknesses
 - The 90-degree rotation settings is over-simplified to some extent. It is easier for the hypernetwork to learn the G-equivariant parameters compared with a larger rotation group. Especially in the linear layer setting, if the rotation degree is not in {0, 90, 180, 270}, the rotated feature cannot be easily represented as permutation which is the premise of the hypernetwork design. The extension to $D_{4n}$ is not a trivial solution, as it requires forwarding both the hypernetwork and the main CNN $|D_{4n}/Z_4|$ times, significantly increasing computational and memory costs. This approach also reduces the technical novelty, as equivariant features can be obtained by feeding multiple rotated input images to a static CNN.
- The current presentation, especially equations and figures, is a bit hard to interpret. For example, in Line 204, what’s the dimension of the output $a^i$. The connection between Figure 2 and the text description of the filter decomposition is not clear. The notation used throughout the paper needs to be more consistent and precise.
- The proposed method does not show competitive results compared with the given limited benchmarks, especially in experiments with deeper CNNs on the CIFAR-10/100 datasets. The baselines used for comparison are also somewhat outdated, which makes the experimental validation less convincing. The performance gap is particularly noticeable on more complex datasets, suggesting the method might not scale well.

### Questions
-Could you please elaborate on the detailed hypernetwork design used in the experiments?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Equivariant deep learning methods have seen a growing amount of research interest over recent years as model paradigm of choice for small datasets with known symmetries. However, these methods have been shown ot scale poorly with more data, as the computational overhead or symmetry-specific constraints impede the optimization of such networks. This paper proposes a novel GCNN architecture that attempts to address these constraints. Authors propose to do this by parameterizing the weights of their equivariant model through a non-equivariant hypernetwork. Equivariance is achieved by augmenting the input data according to the group of choice, passing the data through this hypernetwork and composing the resulting output kernels and linear layers according to the group action. The resulting parameterized network, which the authors show to be equivariant by construction, is then used to e.g. classify the input data. Authors propose a number of methods to reduce the computational overhead of this approach, and ultimately show experimental results on a number of vision classification benchmarks - showing better or competitive performance to previous equivariant methods.

### Strengths
- The paper is well-written (save for some minor spelling/grammar mistakes), making the matter easy to understand. The complex concept of equivariance in deep learning is introduced in a very accessible manner.
- The proposed method is innovative, as it allows for using any non-equivariant base model to achieve an equivariant framework. This approach is different from canonicalization-based methods, as it retains its equivariance property throughout the network, arguably a desirable property in complex vision tasks with multiple objects/object-parts under different relative poses.
- The model's performance in experiments is strong compared to other equivariant deep learning baselines, achieving better or competitive performance in classification on CIFAR10/100 and STL10.
- The paper contains illustrative figures that aid understanding of the work.

### Weaknesses
 - My main concern is with respect to the computational overhead that your method imposes. Every input sample needs to be passed through the NEP $|G|$ times, and as you yourself indicate, the resulting network parameters are sample-specific i.e. batched application of the same resulting kernel is not possible without averaging the sample-specific parameters over the batch. It would be good to indicate how your method compares in terms of memory and computational efficiency to base CNN and G-CNN models. It seems to me this computational requirement might be prohibitive in applying your model to larger-scale data (e.g. imagenet which has 224x224 resolution). Could you comment on this?
- The experimental validation of this method is somewhat limited. Especially the results in Sec. 5.1 are hard to valuate, the authors seem to intentionally have chose a very weak baseline (96% on MNIST can easily be achieved by simple MLPs), but i'm not sure why they chose this base model. It makes the results in this table very hard to judge on how informative they are. I think it would be worthwhile to additionally include results for non-invariant tasks (e.g. segmentation).
- If you're okay with performing $|G|$ forward passes per sample, why not simply apply a non-equivariant model directly to the augmented samples and treating the stacked outputs as an equivariant feature map, possibly performing a group-invariant projection over the results? This would also yield a model equivariant/invariant to the group action and is arguably simpler, no?
- Your main motivation is to lift the constraints that equivariance imposes on model architectures and their optimization. However, isn't your hypernetwork by construction also constrained by the same equivariance constraints that G-CNN filter kernels have? In G-CNNs kernels are constructed by transforming a "canonical" kernel under $g\in G$. This construction leads to specific constraints on the optimization: any gradient update is invariant to transformations of an image with $g\in G$. Aren't your kernels constructed in much the same way, leading to the same constraints on gradient updates as in the original G-CNN formulation? What then would be the reason for improved performance of your method compared to G-CNN baselines?

### Questions
- Could you please expand on how your work relates and contrasts from the work of Zhdanov et al [1], who also use a hypernetwork-based approach to parameterize steerable convolutional kernels? I think it might be good to mention this work.
- Could you provide details on the computational complexity of your method, i.e. its runtime and memory efficiency compared to the base CNN and G-CNN models? I think this is an important factor to consider in the evaluation of your work, as it might help the reader gauge how well your method would scale to larger-scale data.


[1] Zhdanov, M., Hoffmann, N., & Cesa, G. (2024). Implicit convolutional kernels for steerable CNNs. Advances in Neural Information Processing Systems, 36.

### Soundness
3

### Presentation
3

### Contribution
2
