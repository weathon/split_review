### Summary

This paper proposes a new method for text-video retrieval. The method consists of two stages. In the first stage, it uses a cosine similarity network to get initial retrieval candidates. In the second stage, it introduces a multi-grained video-text cross attention module to further refine the retrieval results. The authors conduct experiments on several text-video retrieval benchmarks and demonstrate the effectiveness of the proposed method.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The proposed method is simple and easy to understand.
2. The proposed method achieves good performance on several text-video retrieval benchmarks.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The proposed method is a combination of existing techniques, including cosine similarity network, cross attention, and frozen vision encoder. The authors should discuss the novelty of the proposed method in detail.
2. The authors should provide more details about the proposed method, such as the training and inference details.
3. The authors should compare the proposed method with more recent methods, such as CLIP4Clip, X-Pool, and A-CLIP.
4. The authors should conduct experiments on more datasets, such as MSR-VTT and ActivityNet.
5. The authors should provide more ablation studies to analyze the effectiveness of the proposed method.

### Suggestions

The paper would benefit significantly from a more thorough discussion of the novelty of the proposed method. While the individual components (cosine similarity network, cross-attention, and frozen vision encoder) are not novel in themselves, the specific way they are combined and applied to the text-video retrieval task needs to be clearly articulated. The authors should explicitly address how their approach differs from existing methods that also leverage these components. For instance, they should detail the specific architecture of the multi-grained video-text cross-attention module and how it differs from standard cross-attention mechanisms. A detailed explanation of the token selector's role and its interaction with the cross-attention module is also needed. Furthermore, the authors should provide a more in-depth analysis of the computational complexity of their method compared to existing approaches, especially considering the use of a frozen vision encoder. This would help to justify the proposed method's efficiency and effectiveness.

To strengthen the paper, the authors should provide more detailed information about the training and inference procedures. This includes specifying the exact loss functions used, the optimization algorithms, and the hyperparameter settings. For the training process, it is crucial to describe how the multi-grained video-text cross-attention module is trained, including the specific loss function and the optimization strategy. For inference, the authors should provide a clear explanation of how the top-k candidates are selected from the initial retrieval results and how the refined retrieval results are obtained. The authors should also discuss the computational cost of the proposed method during both training and inference, including the time and memory requirements. This information is essential for assessing the practical applicability of the proposed method. Furthermore, the authors should provide a more detailed analysis of the impact of different hyperparameter settings on the performance of the proposed method.

Finally, the authors should conduct a more comprehensive experimental evaluation of their method. This includes comparing their method with more recent state-of-the-art methods, such as CLIP4Clip, X-Pool, and A-CLIP, on a wider range of datasets, including MSR-VTT and ActivityNet. The authors should also conduct more ablation studies to analyze the effectiveness of different components of their method. For example, they should investigate the impact of removing the multi-grained video-text cross-attention module or using different token selection strategies. These ablation studies should be designed to isolate the contribution of each component to the overall performance of the proposed method. The authors should also provide a more detailed analysis of the results, including error analysis and visualization of the retrieval results. This would help to better understand the strengths and weaknesses of the proposed method.

### Questions

Please see the weaknesses.

### Rating

3: reject, not good enough

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
