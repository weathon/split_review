# PRF: Parallel Resonate and Fire Neuron for Long Sequence Learning in Spiking Neural Networks

- Decision: Reject
- Scores: 6, 8, 5, 3

## Abstract
Recently, there is growing demand for effective and efficient long sequence modeling, with State Space Models (SSMs) proving to be effective for long sequence tasks. To further reduce energy consumption, SSMs can be adapted to Spiking Neural Networks (SNNs) using spiking functions. However, current spiking-formalized SSMs approaches still rely on float-point matrix-vector multiplication during inference, undermining SNNs' energy advantage. In this work, we address the efficiency and performance challenges of long sequence learning in SNNs simultaneously. First, we propose a decoupled reset method for parallel spiking neuron training, reducing the typical Leaky Integrate-and-Fire (LIF) model's training time from $O(L^2)$ to $O(L\log L)$, effectively speeding up the training by $6.57 \times$ to $16.50 \times$ on sequence lengths $1,024$ to $32,768$. To our best knowledge, this is the first time that parallel computation with a reset mechanism is implemented achieving equivalence to its sequential counterpart. Secondly, to capture long-range dependencies, we propose a Parallel Resonate and Fire (PRF) neuron, which leverages an oscillating membrane potential driven by a resonate mechanism from a differentiable reset function in the complex domain. The PRF enables efficient long sequence learning while maintaining parallel training. Finally, we demonstrate that the proposed spike-driven architecture using PRF achieves performance comparable to Structured SSMs (S4), with two orders of magnitude reduction in energy consumption, outperforming Transformer on Long Range Arena tasks. \footnote{The GitHub repository will be released after paper accepted.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce a new spiking neuron model, the parallel resonate and fire (PRF) neuron, that has two advantages over the classic leaky integrate-and-fire (LIF) neuron.

1) it is parallelizable and thus speeds up training and inference times

2) it has a longer-term memory because it can resonate.

### Strengths
The accuracy on the LRA benchmark is trully impressive, almost as good as S4, while it could consume much less energy (at least in theory).

### Weaknesses
* The accuracy on spMNIST is much less convicing. Here two similar recent proposals are much more accurate: Li et al 2024 (cited) and Bal et al 2024 (cited)
These refs should be added to Table 2.
I also suggest adding sequential CIFAR, which is more challenging.

* Other parallel spiking neuron models should be cited and added to Fig 4 left and to the comparison tables when possible, and the differences/similarities should be highlighted:  Fang et al 2023 (cited), Chen et al 2024, Yarga et al 2024

* The resonance seems similar to Baronig et al. 2024, which should be cited, and the differences/similarities should be highlighted.

### Questions
* Any idea why Li et al 2024 does better than you on psMNIST, but not on LRA?

* L244 "At this point, all recursive forms have been converted into dynamic equations." I agree, but still, the dynamic equations should presumably be solved sequentially. So, I don't see how this helps parallelization. More insight is needed here.

* According to Fig 2 the residual connections carry floats, not spikes. This could be a pb for implementation on neuromorphic chips. Could the authors elaborate?

* L505 "This energy reduction mainly benefits from the extreme sparsity of spikes"
Could even higher levels of sparsity could be encouraged via some additional terms in the loss function?

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
4

### Summary
This paper focuses on SNNs for long sequence learning. It first reformulates the reset mechanism of the LIF model into an iterative form to enable parallel training. The authors then propose the PRF neuron to enhance the modeling of long-range dependencies. Both theoretical and experimental results demonstrate the effectiveness and efficiency of the proposed methods.

### Strengths
- The paper is well-written and easy to read, with excellent presentation. The proposed methods are novel.

- The experiments and analyses are comprehensive. The performance improvements on the challenging LRA tasks in terms of both efficiency and accuracy are significant.

- The PRF neuron shows promise for deployment on neuromorphic chips for inference.

### Weaknesses
 - The reset mechanism cannot be computed in parallel with the membrane potential integration process, indicating that the overall neuron model is not fully trained in parallel.

- There is a lack of comparison with existing parallel spiking neuron models, such as the PSN family models [1] and PMSN [2] models.

### Questions
- What are the connections between the proposed PRF neuron and SSMs?

- What impact does the reset have on the performance of the PRF model in LRA tasks?

- The existing PSN and PMSN models also aim to address the challenges of parallel training and modeling long-range dependencies. Please discuss the differences between PRF and these models.

[1] Parallel Spiking Neurons with High Efficiency and Ability to Learn Long-term Dependencies.

[2] PMSN: A Parallel Multi-compartment Spiking Neuron for Multi-scale Temporal Processing.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a decoupled reset method for parallel training of spiking neurons, significantly improving the training speed of LIF neurons. Additionally, a parallel mechanism is introduced into the Resonate-and-Fire model, combined with the SD-TCM structure to achieve efficient long-sequence learning. This approach significantly reduces model energy consumption while achieving comparable performance to SSM (S4) and outperforming Transformer in LRA tasks. However, the experimental section is incomplete, particularly the ablation studies. Furthermore, the motivation behind the reset mechanism is not clearly described. Additional experiments are recommended to further validate the proposed approach.

### Strengths
1. This paper proposes a decoupled reset-based parallel training strategy, reducing the training time complexity of LIF neurons to O(LlogL). The authors claim this is the first application of the reset mechanism in parallel training.

2. The paper introduces a parallel mechanism into Resonate-and-Fire neurons, enhancing the model's temporal processing capability.

3. The paper presents the SD-TCM architecture, which, combined with PRF neurons, was tested on LRA tasks. The authors claim it achieved performance comparable to SSM (S4).

### Weaknesses
1. The proposed method's long-sequence learning capability is mainly validated in Section 5.2. However, this validation is limited to the S/PS-MNIST image sequence task, with only marginal improvements compared to current SOTA models. The experiments do not sufficiently demonstrate the method's effectiveness on more complex sequence tasks, such as those involving variable-length inputs or longer temporal dependencies.
2. The study lacks effective ablation experiments. In Section 5.3, the model's performance on LRA tasks is evaluated, but the contribution of the SD-TCM structure to the performance was not verified, and the improvement was solely attributed to the temporal processing capability of RF neurons. The paper needs a more thorough analysis of the SD-TCM components to justify their inclusion.
3. The paper combines Figures 1(d) and (e) to illustrate the strong temporal processing capability of RF neurons. However, the experimental section lacks relevant visualizations to further explain why RF neurons are more suitable for temporal tasks compared to LIF neurons. There is a lack of direct experimental evidence linking the theoretical advantages of RF neurons to their observed performance gains.
4. The research motivation is unclear. The abstract claims that this is the first implementation of a parallel reset mechanism, yet the experimental section does not evaluate its impact on performance. The paper should explicitly quantify the benefits of the proposed reset mechanism, such as training speed or convergence rate, and compare it to alternatives.
5. The reproducibility of the experiments is limited. The experimental section should include multiple trials to further validate the proposed method's effectiveness.

### Questions
1. To my knowledge, removing the reset mechanism might be the simplest and most effective approach. Several existing studies have explored parallel implementations, such as PSN[1]. The authors should include an experiment to compare their method with these approaches.
2. The paper validates the proposed method on the S/PS-MNIST dataset and claims to achieve SOTA results. However, the performance on other image sequence datasets is not significant. I suggest that the authors expand the experiments further and compare the proposed method with other advanced sequence models to better demonstrate its advantages.

[1] Fang W, Yu Z, Zhou Z, et al. Parallel spiking neurons with high efficiency and ability to learn long-term dependencies[J]. Advances in Neural Information Processing Systems, 2024, 36.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new decoupled reset method to accelerate training, making the effect of parallel training equivalent to sequential training. This method can increase the back propagation speed by three orders of magnitude and is applicable to all types of spiking neurons. In addition, in order to effectively capture long-term dependencies, this paper designs a new type of PRF neuron, which has an oscillating membrane potential in the complex domain and works through an adaptive differentiable reset mechanism.

### Strengths
1. This paper integrate PRF neurons into the SD-TCM module, which performs comparable to S4 in long-term dependency tasks while reducing inference energy consumption by two orders of magnitude.
2. Improved the previous SNN parallel method to achieve acceleration, and achieved good results on the lra dataset.

### Weaknesses
1. Since there is no code in the appendix of this article, I have doubts about the authenticity of lra's experimental results.
2. There are too many typos in the article. The citation format of the whole article should be “\citep{}” instead of  “\cite{}”. At the same time, please use the same “spike-driven” format throughout the article.
3. The comparison in Figure 1 is unfair, as SSM is a block and the proposed PRF is just a neuron. This makes the complexity comparison unfair.
4. In addition, I have doubts about the effectiveness of the proposed method. In Table 4, we can see that the improvement gains of different modules are very low. Does this mean that the proposed method relies heavily on its own architecture? Please add additional ablation experiments on other architectures.

### Questions
see weakness bellow.

### Soundness
2

### Presentation
2

### Contribution
2
