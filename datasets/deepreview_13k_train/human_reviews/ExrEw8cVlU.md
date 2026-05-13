# Poison-splat: Computation Cost Attack on 3D Gaussian Splatting

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
3D Gaussian splatting (3DGS), known for its groundbreaking performance and efficiency, has become a dominant 3D representation and brought progress to many 3D vision tasks. However, in this work, we reveal a significant security vulnerability that has been largely overlooked in 3DGS: \textbf{the computation cost of training 3DGS could be maliciously tampered by poisoning the input data}. By developing an attack named \textit{Poison-splat}, we reveal a novel attack surface where the adversary can poison the input images to \textbf{drastically increase the computation memory and time} needed for 3DGS training, pushing the algorithm towards its worst computation complexity. In extreme cases, the attack can even consume all allocable memory, leading to a Denial-of-Service (DoS) that disrupts servers, resulting in practical damages to real-world 3DGS service vendors. Such a computation cost attack is achieved by addressing a bi-level optimization problem through three tailored strategies: attack objective approximation, proxy model rendering, and optional constrained optimization. These strategies not only ensure the effectiveness of our attack but also make it difficult to defend with simple defensive measures.}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces Poison-splat, a data poisoning attack targeting the training phase of 3D Gaussian Splatting (3DGS). It exposes a vulnerability in the adaptive model complexity of 3DGS, showing how manipulated input data can significantly escalate computation costs during training, potentially resulting in a Denial-of-Service by consuming all available memory.

### Strengths
+ A unique computation cost attack targeting 3D Gaussian Splatting.
+ Highlights practical vulnerabilities in commercial 3D reconstruction services.
+ Thorough experimentation across various datasets.

### Weaknesses
 - The paper frames the problem as a data poisoning attack. However, it does not clearly elaborate on the poisoning ratio required for Poison-Splat to be effective. Additionally, the implications of varying poisoning ratios, particularly their impact on the stealthiness and overall effectiveness of the attack, are not thoroughly discussed. It remains unclear how the attack's efficacy scales with the proportion of poisoned data, and whether lower poisoning ratios can still lead to significant resource consumption. A more detailed analysis of this trade-off is needed.

- The paper mentions that Poison-Splat maximizes the number of Gaussians by enhancing the sharpness of 3D objects through controlling the smoothness factor. However, it is not clearly explained how the smoothness threshold is defined to ensure an effective attack. Additionally, the impact of this threshold on the stealthiness of the attack remains unclear. The mechanism by which the smoothness factor influences Gaussian proliferation needs further clarification, and the sensitivity of the attack to different smoothness parameters should be explored.

- Algorithm 1 indicates that generating backdoor samples with Poison-Splat requires a quadratic time complexity relative to the number of iterations, which raises concerns about the practicality of this approach during training. The computational cost of generating poisoned data, especially in relation to the training time of the 3DGS model itself, needs to be more thoroughly examined. The paper should provide a more detailed analysis of the time complexity and its real-world implications.

- Would the Poison-Splat technique maintain its effectiveness when the 3DGS algorithm is trained in a multi-GPU environment? Additionally, the attack should be assessed on various GPUs with different clock frequencies and memory bandwidths to evaluate the generalizability of the approach. The paper should investigate whether the attack's effectiveness is consistent across different hardware configurations, including variations in GPU memory and processing power.

- The paper states a basic defense against Poison-Spat by limiting the number of Gaussians, but it does not specify the threshold for the number considered in this defense. It would be beneficial to include an evaluation that explores the effect of varying these Gaussian limits. The effectiveness of this defense mechanism needs to be quantified, and the trade-off between defense strength and reconstruction quality should be analyzed.

- The definition of the threat model for the Poison-Splat attack could be more precise, particularly in specifying attacker capabilities and constraints. Explicitly define white-box and black-box scenarios for the proxy model. The paper should clearly delineate the attacker's knowledge and capabilities in different attack scenarios, including access to model parameters and training data.

- Why does the attack perform well on specific datasets in the white-box scenario but less effectively on others, such as the Tanks-and-Temples data (as shown in Table 1 and Table 3)? Can authors provide additional reasoning? The paper should provide a more in-depth analysis of the factors that contribute to the varying attack performance across different datasets, including scene complexity and camera configurations.

### Questions
1. What poisoning ratio is needed for Poison-Splat to be effective, and how does it affect stealth and impact?
2. How is the smoothness threshold defined, and how does it impact the stealth of the attack?
3. Does the quadratic time complexity of Algorithm 1 raise practical concerns during training?
4. Is Poison-Splat still effective in multi-GPU settings, and how does it perform across GPUs with different specs?
5. What is the Gaussian limit threshold in the basic defense, and how do varying limits affect the attack?

### Soundness
3

### Presentation
4

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
This paper proposes an adversarial attack against 3D Gaussian splatting, aiming at increasing the computational cost of this process. Their attack is based on the flexibility of this algorithm, in which the computational cost will change dynamically according to the input image features. Their attack named poison-splat leverages a proxy 3DGS model and the improvement of the total variation score to increase the number of gaussians required in computation, hence bring a huge computational cost regarding GPU memory usage and training time. Their evaluation has included both white-box and black-box attack results and discussed simple defense strategies.

### Strengths
1. This work identifies a new kind of vulnerability in 3DGS systems, which is the computational cost attack.
2. Authors have proposed an efficient algorithm to optimize a perturbation to increase the number of gaussians required in 3DGS.
3. The presentation of the paper is clear and easy to follow.
4. Evaluation results demonstrate the good attack performance in both black-box and white-box settings.

### Weaknesses
1. The constraint of the perturbation (epsilon = 16/255) seems large, and the quality of the resulted image could be affected. More ablation studies may be conducted to evaluate other constraint thresholds. 
2. A simple defense might be smoothing the input images before conducting 3DGS, which seems an adaptive defense regarding your perturbations to the input. You may discuss or evaluate the effectiveness and negative impact of such defense.

### Questions
1. Since there are many online services using 3DGS, as you mentioned in the paper, have you evaluated the real-world attack performance of your technique on those application? Will the responding time be extended or causing deny of service?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper discovers a security vulnerability in 3DGS. It shows that the computation cost of
training 3DGS could be maliciously tampered by poisoning the input data. An attack named Poison-splat is presented.

I have read the response of the authors and the comments of other reviewers. I would recommend weak accept.

### Strengths
1. The paper is well written and organized.
2. The paper reveals that the flexibility in model complexity of 3DGS can become a security backdoor, making it vulnerable to computation cost attack.
3. Attacks are formulated and extensive experiments are conducted.

### Weaknesses
1. Is the attack practically feasible in real-world scenarios, or is it only feasible in theory?
2. In the work, the authors approximate the outer maximum objective with the number of Gaussians, which appears to be a theoretical assumption that may not apply in real-world scenarios.

### Questions
My concerns mainly lie in the practically feasible of the proposed attack.
1. Is the attack practically feasible in real-world scenarios, or is it only feasible in theory?
2. In the work, the authors approximate the outer maximum objective with the number of Gaussians, which appears to be a theoretical assumption that may not apply in real-world scenarios.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work reveals a major security vulnerability that has been overlooked in 3D Gaussian Splatting (3DGS): the computational cost of training 3DGS can be maliciously manipulated by poisoning the input data. This paper introduces a novel attack, termed "Poison," in which an adversary can poison the input images, thereby significantly increasing the memory and computational time required for 3DGS training, ultimately pushing the algorithm to its highest computational complexity. In extreme cases, the attack can even exhaust all available memory, leading to a denial-of-service (DoS) event on the server and causing real harm to 3DGS service providers.
The attack is modeled as a two-layer optimization problem, addressed through three strategies: attack target approximation, proxy model rendering, and optional constrained optimization. This proposed approach not only ensures the effectiveness of the attack but also makes it challenging for simple, existing defenses to succeed. This novel attack aims to raise awareness of the potential vulnerabilities in 3DGS systems.

### Strengths
1. It reveals a major security vulnerability that has been overlooked in 3DGS.
2. The attack's effectiveness is validated across various datasets.

### Weaknesses
1. It lacks evaluation of the attack's effects on the inference phase.
2. There are no intuitive metrics for evaluating the success or failure of this attack.

### Questions
(1) As a model training service provider, certain benchmarks, such as model size and typical training duration, are commonly understood. Given these expectations, would an attack that poisons samples to increase memory usage and training time be easy to detect? Additionally, could existing methods for detecting adversarial samples be effective in identifying these poisoned samples?
(2)Are existing attack methods targeting the inference phase applicable to the training phase? If so, could these methods be included in the experimental analysis for comparison? If not, could the authors explain why?
(3) Since this attack targets the training phase, it would be helpful if the authors could analyze the required percentage of contamination in a clean dataset for the attack to succeed.
(4) In the Experimental Analysis section, the authors conducted extensive experiments to analyze the impact of the attack on memory usage and training duration, which is commendable. However, while the abstract suggests that Poison-splat can lead to a DoS damage to the server, the Experimental Analysis section lacks any evaluation of the attack's effects on the inference phase.
(5) Could the authors add more common models to compare the effectiveness of black-box and white-box attacks?
(6) The primary objective of the attack is to consume excessive computational resources, but what are the most serious consequences of this? Is it a denial-of-service (DoS) scenario? Additionally, how difficult would it be to achieve significant damage? For instance, if an attacker aims to prevent a model from completing its training, would this require prior knowledge of the service provider's computational resources? Lastly, it is unclear how the success or failure of this type of attack should be assessed. For example, if the service provider’s computational resources are sufficient to handle the increased demand, should the attack then be considered unsuccessful?

### Soundness
4

### Presentation
4

### Contribution
4
