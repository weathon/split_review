# Soft Contrastive Learning for Time Series

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Contrastive learning has shown to be effective to learn representations from time series in a self-supervised way.
However, contrasting similar time series instances or values from adjacent timestamps within a time series leads to ignore their inherent correlations, which results in deteriorating the quality of learned representations.
To address this issue, we propose \textit{SoftCLT}, a simple yet effective soft contrastive learning strategy for time series.
This is achieved by introducing instance-wise and temporal contrastive loss with soft assignments ranging from zero to one.
Specifically, we define soft assignments for 1) instance-wise contrastive loss by the distance between time series on the data space, and 2) temporal contrastive loss by the difference of timestamps.
SoftCLT is a plug-and-play method for time series contrastive learning that improves the quality of learned representations without bells and whistles.
In experiments, we demonstrate that SoftCLT consistently improves the performance in various downstream tasks including classification, semi-supervised learning, transfer learning, and anomaly detection, showing state-of-the-art performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors address challenges in time series data annotation and the limitations of standard contrastive learning (CL) in representing TS data. Key contributions of the paper are:

- Introduction of SoftCLT, a soft contrastive learning strategy tailored for time series data. Their framework can be adapted to other CL frameworks relatively easily.
- The proposal of soft contrastive losses for both instance and temporal dimensions, addressing the shortcomings of existing CL methods for TS.
- Comprehensive experimental evidence demonstrating that SoftCLT enhances state-of-the-art performance across multiple TS tasks.

### Strengths
The submission has the following strenghts:

- Ablation study is present and seems to demonstrate the usefulness of the proposed additions.
- Compared to the selected baselines (emphasis on selected), the model performs well.
- I appreciate that the authors have chosen to go for a more detailed analysis of the representation learning abilities of their model. By this I mean that rather than considering only task-performance, they also investigate aspects such as robustness to non-stationarity, and also semi-supervised learning. This is usually absent from related papers.
- The ideas are well explained, the paper is clear.

### Weaknesses
The submission has the following weaknesses:
- Problem with the comparisons. Entirely absent from the main paper is any comparison with CoST [1], or any more recent contrastive approach. While this is a single issue it is one I am quite concerned about. Similarly, a comparison to recent approaches in the regression setting of TS2Vec (nothing prevents that comparison, the TS2Vec code works seamlessly for both approaches). My reasoning is that the proposed idea is interesting, but also relatively simple. This is fine in general: simple ideas bring value in research as well. However, coupled with a lack of comparison to recent approaches, it is very difficult to ascertain the value of the contribution.

Currently this is enough for me to not recommend acceptance, but as noted in the questions section, I am willing to update my score should the authors adress this.

### Questions
As noted in the Weaknesses section, I would like a detailed comparison with CoST and an evaluation in the regression setting. If the authors provide this, and the results warrant it, I will raise my score.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study argues that when using time series data in contrastive learning, contrasting ( between positive and negative) instances or values located in proximity can lead to the neglect of their inherent correlation. Therefore, they introduce a continuous (referred as soft) weighting approach as an alternative to binary labeling, serving as a generalization of the standard contrastive loss, with the transformation occurring when replacing soft assignments with hard assignments of zero for negatives and one for positives. For soft assignment, the authors take into account two aspects: the similarity between two time series in data space and the proximity of two time series with respect to their timestamps.

### Strengths
The papers is well written and clear. The figures presented help to clarify the main idea and how it is implemented. The idea is novel for the simplified setup that is considered. The experimental results cover 3 downstream tasks and comprehensively evaluate the assumed setup.

### Weaknesses
The paper addresses a simplified scenario in which issues related to noise, seasonality, and non-stationarity are not considered, as there is no apparent mechanism in the approach to address these prevalent challenges found in real-world time series data.
Regarding robustness in the presence of noise and non-stationarity there  is no specific discussion or empirical evaluation.  Regarding seasonality, the authors mentioned "Our conjecture is that TS in the real world usually do not exhibit the perfect seasonality, as indicated by the ADF test result, such that SoftCLT takes advantage of the non-seasonal portions." While perfect seasonality may be absent in some datasets and may vary in intensity across different datasets, I believe completely disregarding it is not a practical approach.

### Questions
Can this case be elaborated a bit further:” when α = 1, we give the assignment of one to the pairs with the distance of zero as well as the pairs of the same TS” What if in the same TS we are experiencing two different patterns, shifts or different distribution

In equation 3, augmentation for I and i+N, how it  is performed? What if there is only a shift in the pattern in the instances, otherwise there are very similar how you address this in your computation, It would be great to include an illustration for this case to show you approach is robust to shift (or some noise) which is very common in real world applications.


How do you manage non stationary in the time series, where the immediate next point might be the start of a different distribution? How your similarity comparison handles it when the the proximity is assumed to have high similarity which is not necessarily true.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study introduce a new method of performing constrastive learning, a soften version of normal positive-negative strategy. These soft assignments are determined by the distance between time series in the data space for instance-wise contrastive loss and the difference in timestamps for temporal contrastive loss.

### Strengths
Contribution:

- The idea of soft constrastive learning is straight-forward and natural. The underlying functions are widely-adopted and straightforward to implement.
- The experiments are extensive and cover many time-series tasks (classification, anomaly detection) as well as scenario (self/semi supervised and supervised learning). The comparison with soft-CL techniques from other domains and ablation study make the whole experimental section be quite well-rounded.

Representation:

- Intuitive and direct illustrations via Figures (e.g. Fig.1, 2)

### Weaknesses
 - Contribution:
    - For instance-wise CL:
        - the use of DTW might be a potential bottleneck in case of dealing with lengthy time-series. While the authors suggest the use of FastDTW, the complexity regarding the memory might be increased, and also the potential reduce in approximation (in case the warping path between two time series instances is highly nonlinear). In other words, the choices of DTW or FastDTW are hurting the pipeline in some ways.
        - the calculation of weight based on the distance in the data space. However, this make the weighting process be dependent on the scale of input data. Together with the wrapper of Sigmoid function, it might be saturated upon too large or too small input. This effect might make the weights not representative to use in instance-wise CL. While empirically, it illustrates the effective over in latent space, more effort need to be done to consider on which space one should rely on to calculate distance.
    - For temporal-wise CL, the current weight assignment implicitly assume the data from neighbors’ timesteps should be weighted heavier than the data from far timesteps. However, that behavior might not always hold true, as illustrated in work of Tonekaboni (2021).



### Questions
The authors please address or provide answers to any questions from the weaknesses listed.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a new contrastive learning method for time series. Specifically, they propose to remove the hard positive/negative assignment from the original NCE by a soft reweighting incorporating prior information about the temporal closeness or similarity of inputs. The authors evaluate their method on various time series-related tasks showing strong improvement compared to "hard" CL methods. They also provide ablation experiments concerning their new objective hyperparameters.

### Strengths
This paper is of high quality with the following strengths: 

- Overall very well-written paper with an easy-to-follow structure, in particular:
    - Related work is structured and extensive (with the exception mentioned below in weaknesses).
    - Method is clear and figures relevant making the method easy to understand.
    - Experiments are very extensive and well described both in the manuscript and the supplementary materials.

- I appreciate that despite introducing numerous components and hyperparameters ( temperature, distance metric, weight function, etc..), authors provide ablations to each of these components. 
- The authors discussed the additional computational complexity of their method and in particular DTW known to have a squared complexity. 
- The amount of experiments carried out is very large and diverse

### Weaknesses
There are, however, some weaknesses, in particular in terms of related work, which I detail below:


**Related work**
As mentioned the related work is extensive but misses some seminal works regarding contrastive learning methods for time series tackling the challenges of inter/intra samples dependencies:
- First, "Subject-aware contrastive learning for biosignals" by Cheng et al (2020) proposes to only use negative representations from the same time series to "promote subject-invariant" representation, what the authors would refer to as "temporal CL".
- Second, "CLOCS: Contrastive Learning of Cardiac Signals Across Space, Time, and Patients" by Kiyasseh et al. (2021) proposes to on the contrary use representations from the same time series as positives, what the authors would refer to as "instance-wise CL". This is similar to TNC but with a neighborhood being defined as being from the same time series. 
- Finally, and more importantly, "Neighborhood Contrastive Learning Applied to Online Patient Monitoring" by Yeche et al. (2021), introduces the trade-off used by the authors between instance-wise and temporal-wise CL controlled by $\lambda$. In particular, the objective proposed by Yeche et al., namely NCL, is similar to taking a hard assignment for instance-wise CL $w_I(i,j) = \mathbb{1}_{[i = j]}$ and a (discontinuous) uniform one over a window for temporal CL. 

Thus, I think it's really important that this work refers to these three works and in particular NCL from which the SoftCLT is an extension to continuous neighborhood definitions. It would be nice to have a comparison to it as well. 


**Clarity**

- The authors refer multiple times to instance-wise and temporal CL before defining it properly in the method section. I think pointing the reader to this section or defining the terms in the introduction could improve clarity.

- referring to a "temperature" parameter $\tau_t$ and $\tau_i$ can be quite misleading in the context of contrastive learning, where this term was coined by Chen et al. (2020), in the simCLR paper. (See my comment below on the choice of assignment function) Given the assignment function is some form of Laplacian kernel, referring to $l =\frac{1}{\tau}$ as a lengthscale parameter would be more coherent with literature and avoid confusion with temperature parameters from previous works on CL. 

**Method**
- The authors define their assignment function around a sigmoid function which is defined over $\mathbb{R}$ whereas its input $D$ lies in $\mathbb{R}^+$. It seems to overcome this, they tweak around their sigmoid function to obtain a symmetric function $w(D) = \frac{2}{1+e^{Dt}}$. Why not rely on existing literature instead and typically use a Laplacian kernel $w(D) = e^{-\frac{D}{l}}$? 
- Exploring further different kernel and their impact on performance would have been a nice addition. In particular, using a generalized Gaussian kernel and looking at the impact of the shape parameter $\beta$ would be nice as $\beta=1$ is SoftCLT and  $\beta=\infty$ is NCL temporal CL. 
- Exploring further the impact of the trade-off between local (temporal) and global (instance) features learning ruled by $\alpha$ would be a nice addition to ablations.
**Conclusion**


Clarity and Method weakness are easily addressable. Regarding related work, despite the similarities with NCL, I still think the contribution to be significant given the novelty around the neighborhood/assignment function and the extent of the experiments on various tasks, justifying my choice of recommending acceptance. However,  I firmly believe the three works I mentioned should be correctly cited in particular the link to Yeche et al. (2021) work.

### Questions
I don't have any questions beyond the points raised in the above sections.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
