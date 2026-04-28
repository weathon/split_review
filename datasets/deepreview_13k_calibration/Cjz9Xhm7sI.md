# High-Dynamic Radar Sequence Prediction for Weather Nowcasting Using Spatiotemporal Coherent Gaussian Representation

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8

## Abstract
Weather nowcasting is an essential task that involves predicting future radar echo sequences based on current observations, offering significant benefits for disaster management, transportation, and urban planning. Current prediction methods are limited by training and storage efficiency, mainly focusing on 2D spatial predictions at specific altitudes. Meanwhile, 3D volumetric predictions at each timestamp remain largely unexplored. To address such a challenge, we introduce a comprehensive framework for 3D radar sequence prediction in weather nowcasting, using the newly proposed SpatioTemporal Coherent Gaussian Splatting (STC-GS) for dynamic radar representation and GauMamba for efficient and accurate forecasting. Specifically, rather than relying on a 4D Gaussian for dynamic scene reconstruction, STC-GS optimizes 3D scenes at each frame by employing a group of Gaussians while effectively capturing their movements across consecutive frames. It ensures consistent tracking of each Gaussian over time, making it particularly effective for prediction tasks. With the temporally correlated Gaussian groups established, we utilize them to train GauMamba, which integrates a memory mechanism into the Mamba framework. This allows the model to learn the temporal evolution of Gaussian groups while efficiently handling a large volume of Gaussian tokens. As a result, it achieves both efficiency and accuracy in forecasting a wide range of dynamic meteorological radar signals. The experimental results demonstrate that our STC-GS can efficiently represent 3D radar sequences with over $16\times$ higher spatial resolution compared with the existing 3D representation methods, while GauMamba outperforms state-of-the-art methods in forecasting a broad spectrum of high-dynamic weather conditions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper presents a novel 3D weather nowcasting approach using high-dynamic radar sequences. The method introduces a SpatioTemporal Coherent Gaussian Splatting technique to efficiently represent the dynamic radar data, which is then processed by the GauMamba network to generate weather forecasts. Additionally, the paper proposes MOSAIC, a new high-resolution 3D radar sequence dataset, containing more than 24K radar observations. Experimental results on both NEXRAD and MOSAIC show that the proposed approach outperforms baseline methods with significant margins.

### Strengths
- The proposed representation and processing pipeline are well-motivated and supported by the experiments, resulting in performance improvements over baseline methods.
- The memory usage of the method remains constant w.r.t. horizontal resolution, in contrast to other baselines with linear memory growth.
- The MOSAIC dataset offers a large dataset of radar echoes that capture meteorological events across multiple years.

### Weaknesses
 - A short discussion of the proposed dataset, MOSAIC, in the main paper could be beneficial to the readers.
- Could the authors clarify the plan for the dataset? Will it be made publicly available, and if so, how to ensure that the dataset can be accessed by the public continuously?
- For the LPIPS evaluation, how is the evaluator model trained? If the model is pretrained with a general-purpose dataset, would it work well with radar data?
- Minor visual artifacts can be seen in Figure 2 (center bottom).

### Questions
Please see Weaknesses.

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
The paper proposed a framework utilizing SpatioTemporal Coherent Gaussian Splatting (STC-GS) for dynamic radar representation and GauMamba for forecasting dynamic meteorological radar signals. The STC-GS established 4D dynamic Gaussians, and the GauMamba utilizes the Mamba framework to predict 3D radar sequences. The experiments on NEXRAD and MOSAIC present superior performance against previous 4D reconstruction methods.

### Strengths
- The writing is comprehensive and easy to follow

- The ablation study is thorough and provides insights into the model design and the selection of hyperparameters.

- By combining Gaussian and Mamba methodologies, the GauMamba model is likely designed to enhance forecasting accuracy, especially in scenarios involving temporal and spatial data complexities which are typical in meteorological datasets.

### Weaknesses
 - Previous research has introduced combinations such as Gamba that combine Gaussian and Mamba model. However, this paper does not sufficiently review these previous works. It would be beneficial to highlight how the proposed GauMamba method differs from earlier studies. Additionally, including comparisons with Mambda + Gaussian baseline methods in the experimental section is crucial for a sufficient comparisons.

- The paper describes experiments conducted on two weather forecasting datasets. These datasets appear to be quite limited, containing only two scenes—if this is incorrect, please advise. Such a small dataset may not adequately demonstrate how the method compares with established baselines. Conducting experiments on larger, more diverse datasets could provide a more thorough evaluation.


### Questions
- The paper mentions employing a group of Gaussian primitives for radar sequence prediction. Is there a fixed number of Gaussian primitives used across all frames, and if so, how is this number determined and maintained throughout the model's operations?

- It is claimed that the GauMamba model is efficient; however, from the comparisons in Figure 4, it appears that at resolutions lower than 256, baseline methods are more memory efficient. Please discuss why there is this discrepancy in memory efficiency at different resolutions and how the baselines' memory scales with increasing resolution.

- Please also discuss the limitations of the proposed method.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a comprehensive framework for 3D radar sequence prediction in weather nowcasting that combines a novel SpatioTemporal Coherent Gaussian Splatting (STC-GS) representation with a memory-augmented predictive network (GauMamba). The approach addresses the key limitations of current 2D prediction methods by enabling efficient and accurate 3D sequence prediction while maintaining computational efficiency.

The main contributions include:

1. A novel 3D radar representation method (STC-GS) that efficiently captures radar data dynamics through bidirectional reconstruction with dual-scale constraints, achieving 16× higher spatial resolution compared to existing 3D representation methods

2. A memory-augmented predictive model (GauMamba) that effectively learns temporal evolution patterns from the STC-GS representations to forecast radar changes, outperforming state-of-the-art methods in prediction accuracy

3. Two new high-dynamic 3D radar sequence datasets:
- MOSAIC: 24,542 single-channel high-resolution radar observations
- NEXRAD: 6,255 six-channel radar observations

### Strengths
Good Originality:
- The paper presents a novel solution for 3D radar sequence prediction by combining Gaussian Splatting with a memory-augmented network
- The adaptation of 3D Gaussian Splatting to dynamic radar data representation represents meaningful innovation in both representation and prediction aspects
- The bidirectional reconstruction pipeline with dual-scale constraints is a creative approach to handle the unique challenges in radar sequence prediction

Good Quality:
- The technical development is thorough with comprehensive theoretical foundations and implementation details
- The experimental evaluation is extensive, covering multiple datasets and comparing with various baselines
- The ablation studies effectively validate the contribution of each component

Good Clarity:
- The paper is well-structured with clear motivation and problem formulation
- The methodology is presented in a logical flow with detailed explanations
- The figures are well-designed and effectively illustrate the key concepts
- The writing is generally clear and easy to follow

Good Significance:
- The work addresses an important practical problem in weather nowcasting
- The proposed framework achieves significant improvements over existing methods:
  * 16× higher spatial resolution in representation
  * 19.7% and 50% reduction in MAE on two datasets
- The introduction of two new high-dynamic 3D radar sequence datasets contributes valuable resources to the research community

> While I support accepting this paper based on its technical merits and clear presentation, I am not very familiar in radar sequence prediction specifically. Therefore, I remain open to adjusting my assessment during the discussion phase based on comments from other reviewers more specialized in this domain.

### Weaknesses
Major Weaknesses: about **Reconstruction Results**

1. Unusual Performance Gap in Reconstruction:
- The results in Table 1 show dramatically better performance compared to baselines
- While authors explain this is due to convergence issues in existing methods, this raises concerns:
  * The performance gap (10× improvement in MAE) seems unusually large
  * Need to consider whether alternative baselines outside 3DGS family might be more appropriate
  * Traditional scene reconstruction methods might provide more reasonable comparisons
 
> Therefore, I would like to suggest the authors to include non-3DGS based methods that might achieve better convergence

2. Missing Qualitative Results:
- The paper lacks visualization results for the reconstruction stage
- This omission is particularly concerning given the significant quantitative improvements claimed
- Visual results would help validate the dramatic performance improvements

> Therefore, I would like to suggest the authors to either:
>   * Add qualitative reconstruction visualizations
>   * OR Provide clear justification for why such visualizations are not included


Minor Weaknesses: Grammar and Writing Issues

- Several grammatical errors throughout the paper
    - For example, on Page 7, line 371

> These should be carefully corrected in the final version

### Questions
Please see Weaknesses

### Soundness
3

### Presentation
3

### Contribution
2
