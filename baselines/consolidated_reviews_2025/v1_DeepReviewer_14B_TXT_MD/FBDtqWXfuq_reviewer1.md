### Summary

This paper proposes a new setting, Modality-Collaborated Federated Learning (MCFL), which focuses on enabling collaboration among uni-modal clients with different data modalities. The authors argue that current federated learning methods primarily focus on uni-modal scenarios or multi-modal clients, which limits their ability to leverage multi-modal data effectively. To address this gap, they introduce a framework called Federated Modality Collaboration (FedCola) based on a modality-agnostic transformer. FedCola explores optimal strategies in cross-modal parameter-sharing, model aggregation, and temporal modality arrangement. The authors conduct comprehensive evaluations demonstrating that FedCola outperforms existing solutions.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper introduces a novel setting in federated learning, emphasizing collaboration between uni-modal clients with different data modalities. This approach shifts away from the traditional focus on multi-modal clients and tasks, making the system more practical for real-world scenarios where clients typically collect data from single modalities.

2. The authors propose a new framework called FedCola, based on a modality-agnostic transformer. FedCola addresses the challenges of model heterogeneity and modality gaps in MCFL by exploring optimal strategies in cross-modal parameter-sharing, model aggregation, and temporal modality arrangement.

3. The paper provides a thorough evaluation of FedCola, comparing it against adapted versions of existing methods like Uni-FedAVG and CreamFL. The evaluation considers various federated learning scenarios, including different numbers of clients, levels of data heterogeneity, and client availability ratios.

### Weaknesses

#### Some Related Works


#### comment

1. The main difference between the proposed MCFL setting and the existing multi-modal federated learning setting is that the final evaluation metric is derived from the individual performances across each modality. This distinction is somewhat subtle and may not be sufficient to justify a completely new setting. The core challenge of aligning cross-modal representations remains, and the paper does not adequately address how the proposed method tackles this challenge in the context of unimodal clients. The evaluation metric, while considering individual modality performance, does not fundamentally alter the underlying problem of learning a shared representation across modalities when explicit cross-modal supervision is absent during local training.

2. The proposed FedCola framework, while utilizing a modality-agnostic transformer, essentially boils down to exploring parameter-sharing strategies and model aggregation schemes within a transformer architecture. This makes it seem more like an application of existing techniques to the new setting rather than a novel technical contribution. The paper lacks a deep analysis of the specific challenges posed by the MCFL setting that would necessitate a novel approach beyond standard parameter sharing and aggregation. The exploration of parameter sharing strategies, while practical, does not introduce a fundamentally new technical insight into how to handle the inherent heterogeneity of unimodal clients in a multi-modal world.

3. The evaluation of FedCola, while comprehensive, primarily focuses on comparing it against adapted baselines in the proposed MCFL setting. It would be beneficial to see comparisons with a broader range of existing multi-modal federated learning methods, even if they are not directly designed for the MCFL setting. This would provide a better understanding of how FedCola stacks up against the state-of-the-art in related areas. The chosen baselines, while relevant, do not fully capture the breadth of existing multi-modal federated learning approaches, particularly those that focus on cross-modal alignment and knowledge transfer.

### Suggestions

The paper introduces an interesting problem setting, but the technical contribution could be strengthened by a more in-depth analysis of the challenges specific to the proposed MCFL scenario. The core issue of cross-modal alignment when only unimodal data is available during local training needs to be addressed more explicitly. The paper should explore how the proposed parameter sharing and aggregation strategies specifically tackle this challenge, rather than simply applying existing techniques to a new problem setting. For example, the authors could investigate the impact of different parameter sharing strategies on the learned representations and analyze how these representations align across modalities. Furthermore, the paper could benefit from a more detailed discussion of the limitations of the proposed approach, particularly in scenarios with high modality heterogeneity or limited data per modality.

To enhance the evaluation, the authors should consider including a wider range of baselines from the multi-modal federated learning literature. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed method compared to existing state-of-the-art approaches. Specifically, it would be beneficial to compare against methods that explicitly address cross-modal alignment and knowledge transfer, even if they are not directly designed for the MCFL setting. The evaluation should also include a more detailed analysis of the impact of different temporal modality arrangements on the final performance, as well as a sensitivity analysis of the proposed modality compensation scheme. This would provide a more complete picture of the effectiveness of the proposed method and its robustness to different experimental conditions.

Finally, the paper should provide a more detailed explanation of the experimental setup, including the specific datasets used, the data partitioning strategy, and the hyperparameter settings. This would allow for a more thorough evaluation of the results and facilitate reproducibility. The authors should also consider releasing their code to the community, which would further enhance the impact of their work. A more detailed discussion of the computational cost of the proposed method compared to the baselines would also be beneficial, as this is an important factor to consider in practical applications.

### Questions

Please see the weakness.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
