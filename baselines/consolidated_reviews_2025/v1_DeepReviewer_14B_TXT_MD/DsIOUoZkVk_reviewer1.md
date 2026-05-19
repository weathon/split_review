### Summary

The paper is theoretical in nature and its main goal is to provide an explanation for the success of contrastive learning algorithms in scenarios that involve unpaired modalities, i.e., where pairs of modalities are observed but not all possible pairs (e.g., audio and text). The authors make three assumptions: conditional independence of modalities given a bridge modality, contrastive learning learning with infoNCE learns the correct density ratio and a assumption about the distribution of the representations (either uniform or Gaussian). Under these assumptions the authors show that the dot product or negative squared distance between representations of unpaired modalities recover the correct marginal density ratio. The authors also argue that a Monte Carlo estimate can be used in the general case where the assumption on the distribution of the representations does not hold. Experiments test the theory on synthetic data and also apply the theory to real data in the context of pre-trained models and reinforcement learning.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper tackles an interesting question on why contrastive learning generalizes to unpaired modalities and the theoretical results seem reasonable. The applications to pre-trained models and reinforcement learning are interesting.

### Weaknesses

#### Some Related Works


#### comment

I have a few concerns about the paper:

1) I did not fully understand the significance of Lemma 3 and the Gaussian assumption. The Gaussian assumption is not needed for the main result to hold, as this is the case for Lemma 2. But I did not understand what Lemma 3 demonstrates.

2) I did not understand the applications to pre-trained models and reinforcement learning. The former seems to argue that because the theory does not hold for CLIP and CLAP, a Monte Carlo estimate is needed to make them work together. But it is not clear to me why this is true and why zero-shot learning does not work. The latter seems to argue that the Monte Carlo estimate is better than direct comparison. But it is not clear why direct comparison is not sufficient and how the Monte Carlo estimate improves on it.

3) The paper makes a few assumptions that are untestable in practice, e.g., Assumption 2. It would be interesting to see an alternative analysis that relaxes these assumptions, perhaps by making milder assumptions about the density.

### Suggestions

The paper would benefit from a more detailed explanation of the role of Lemma 3 and the Gaussian assumption. While Lemma 2 establishes the connection between the density ratio and the dot product under the assumption of a uniform distribution, the purpose of introducing a Gaussian distribution and its connection to the negative squared distance is not clear. It would be helpful to provide a more intuitive explanation of why the Gaussian assumption leads to the negative squared distance and what the implications of this result are. For example, the authors could discuss how the Gaussian assumption might be more realistic in certain scenarios and how this affects the choice of similarity metric. Furthermore, it would be beneficial to provide a more detailed explanation of the constant γ and its role in the theoretical framework. This would help the reader understand the significance of Lemma 3 and its connection to the overall theory.

Regarding the applications, the paper needs to provide more clarity on why zero-shot learning fails for CLIP and CLAP and why the Monte Carlo estimate is necessary. The authors should elaborate on the specific reasons why the assumptions of the theory are not met in this case and how the Monte Carlo estimate addresses these issues. For example, they could provide empirical evidence showing that the assumptions are violated and explain how the Monte Carlo estimate helps to recover the correct density ratio. Similarly, for the reinforcement learning application, the authors should provide a more detailed explanation of why direct comparison is insufficient and how the Monte Carlo estimate improves upon it. It would be helpful to provide a concrete example illustrating the limitations of direct comparison and the benefits of the Monte Carlo approach. For instance, the authors could show how the Monte Carlo estimate is able to capture the full distribution over possible goal states, while direct comparison reduces ambiguous language to averaged embeddings.

Finally, the paper should address the limitations of the assumptions made in the theoretical analysis. While some assumptions are necessary for the theoretical results, it is important to acknowledge that these assumptions may not always hold in practice. The authors should discuss the implications of these assumptions and explore alternative analyses that relax these assumptions. For example, they could investigate the impact of violating Assumption 2 and explore milder assumptions about the density that still allow for meaningful theoretical results. This would make the paper more robust and applicable to a wider range of scenarios. Furthermore, it would be beneficial to provide some empirical analysis of the sensitivity of the results to the assumptions made in the paper. This would help the reader understand the limitations of the theory and the conditions under which it is likely to hold.

### Questions

See above.

### Rating

6

### Confidence

3

**********
