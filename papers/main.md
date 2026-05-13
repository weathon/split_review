

{0}------------------------------------------------

# --- Positional Encodings Anchor Spatial Structure in Vision Transformers: A Geometric Perspective on Robustness ---

Anonymous Author(s)

Affiliation

Address

email

## Abstract

1 Positional embeddings (PEs) in Vision Transformers (ViTs) are known to impact  
2 performance and robustness, but their role in shaping internal spatial representations  
3 is not well understood. In this work, we study how different forms of PEs influence  
4 the representational geometry of ViTs and how these changes relate to robustness  
5 under content-disrupting distribution shifts. We introduce a metric, the Spatial  
6 Similarity Distance Correlation (SSDC), to quantify spatial structure in token  
7 representations. Using this metric, we show that ViTs trained without PEs still  
8 develop non-trivial spatial structure, but this structure is driven by visual content  
9 and collapses under token permutation. In contrast, we find that all PEs considered  
10 (learned absolute, sinusoidal, and rotary) are associated with a consistent shift  
11 toward an index-anchored spatial organization. Representations in these models  
12 remain stable under perturbations that disrupt content, and exhibit substantially  
13 improved robustness to such distributional shifts. We further show that while  
14 different PEs produce distinct depth-wise trajectories of spatial structure, their  
15 robustness properties are largely similar (with secondary variation across encoding  
16 schemes), suggesting that robustness appears to depend on the presence of a  
17 stable positional reference frame more than it depends on the specific encoding  
18 mechanism. These results offer a geometric account of how positional encodings  
19 shape internal representations, with implications for the principled design of future  
20 encoding schemes.

## 21 1 Introduction

22 Vision Transformers (ViTs) model images as sequences of patch tokens processed by self-attention  
23 [Dosovitskiy et al., 2021]. Unlike convolutional architectures, they lack built-in inductive biases  
24 toward locality and translation equivariance, and instead rely on positional embeddings (PEs) to inject  
25 spatial information, enabling the model to distinguish tokens originating from different locations.

26 While PEs are designed to provide positional information, this design does not determine how that  
27 signal is integrated into internal representations. In particular, it remains unclear whether positional  
28 information organizes token representations into similarity structures anchored to absolute indices, or  
29 whether spatial structure continues to arise primarily from visual content.

30 Prior work shows that ViTs retain substantial performance even when positional information is  
31 removed or degraded [Dosovitskiy et al., 2021, Chu et al., 2023], suggesting that spatial relationships  
32 can partially emerge from patch content alone. This raises a central question: if spatial structure can  
33 arise without explicit positional guidance, what functional role do positional embeddings play?

{1}------------------------------------------------

34 Existing studies have largely addressed this question through downstream performance comparisons  
35 or architectural variations. While informative, these approaches provide limited insight into how  
36 positional information shapes internal representations. In particular, it remains unclear whether  
37 different positional encoding schemes (learned absolute, sinusoidal, or rotary) induce distinct spatial  
38 reasoning strategies, or whether their effects on robustness arise from a shared mechanism.

39 In this work, we adopt a geometric perspective. We analyze the evolution of token representations  
40 across the transformer stack using tools from representational geometry [Raghu et al., 2021], introduc-  
41 ing the Spatial Similarity Distance Correlation (SSDC) as a probe of spatial structure. Critically, we  
42 use SSDC in conjunction with a random permutation intervention at inference to distinguish whether  
43 spatial organization is anchored to token indices or driven by patch content. We compare models  
44 trained with learned absolute positional embeddings (APE), sinusoidal encodings (SPE), rotary  
45 embeddings (RoPE), and no positional embeddings, and evaluate their robustness to distributional  
46 shifts.

47 Our central finding is that the specific encoding mechanism matters less than the presence of a  
48 consistent positional signal. We show that:

- 49 • **Positional encodings are associated with index-based spatial organization:** All PE types  
50 shift ViTs away from purely content-driven spatial structure toward representations that  
51 remain partially anchored to token indices under permutation.
- 52 • **This shift, not the encoding form, is associated with robustness:** Despite differing in  
53 how spatial structure develops across depth, APE, sinusoidal, and RoPE models exhibit  
54 broadly comparable robustness to content-disrupting distributional shifts (despite consistent  
55 but smaller differences between encoding schemes), while models lacking index-based  
56 organization are substantially more fragile.
- 57 • **A stable positional reference frame is strongly implicated in robustness:** Using Random  
58 Permutation Training (RPT), which preserves PEs but destroys index-to-location consistency,  
59 we find that robustness is greatly reduced when a consistent positional frame cannot be  
60 learned.

61 Together, these results provide a unified, geometric account of how positional encodings shape internal  
62 representations and why they remain critical for robust visual recognition, though we emphasize that  
63 the evidence is intervention-based rather than strictly causal.

## 64 2 Related Work

###### 65 Positional Information in Vision Transformers

66 The standard Vision Transformer (ViT) breaks the permutation invariance of self-attention by adding  
67 learnable absolute positional embeddings (PEs) to patch tokens [Dosovitskiy et al., 2021], establishing  
68 the dominant paradigm for spatial encoding. However, ViTs retain substantial performance when  
69 positional information is degraded or removed [Dosovitskiy et al., 2021, Chu et al., 2023], suggesting  
70 that spatial structure can partially emerge from patch content alone.

71 Similar observations have been reported beyond vision. Recent work on decoder-only transformers  
72 shows that models trained without PEs can recover positional information implicitly and tend to  
73 rely on relative positions in practice [Kazemnejad et al., 2023]. Earlier findings in convolutional  
74 networks further demonstrate that substantial positional information can be learned implicitly from  
75 architectural biases such as zero-padding [Islam\* et al., 2020]. Together, these results suggest that  
76 explicit positional signals are not strictly required for structured spatial information to emerge.

77 This creates a central puzzle: if spatial structure can arise without explicit positional guidance, what  
78 functional role do PEs play? Prior work has primarily addressed this question through architectural  
79 variants [d’Ascoli et al., 2022, Liu et al., 2021, Heo et al., 2024] or performance comparisons [Doso-  
80 vitskiy et al., 2021, Chu et al., 2023], leaving their mechanistic impact on internal representations  
81 largely unexplored.

###### 82 Representational Analysis of Transformers

83 A separate line of work studies the geometry and dynamics of transformer representations. Early  
84 analyses compare ViT and CNN representations [Raghu et al., 2021], revealing differences in spatial

{2}------------------------------------------------

85 organization. Subsequent work examines how attention transforms representations [Kobayashi  
86 et al., 2021], how representational rank evolves with depth [Dong et al., 2021], and how token  
87 representations tend to homogenize in deeper layers [Bhojanapalli et al., 2021]. The residual stream  
88 framework provides a useful lens for analyzing these dynamics [Elhage et al., 2021]. However,  
89 these approaches do not isolate the causal role of positional embeddings, nor do they connect  
90 representational structure to robustness.

###### 91 Robustness of Visual Models

92 Vision Transformers exhibit distinct robustness profiles compared to convolutional networks. Prior  
93 work shows that transformers are generally more robust to certain spatial perturbations but can  
94 be more sensitive to texture-based changes [Bhojanapalli et al., 2021]. Additional studies report  
95 favorable out-of-distribution generalization properties for ViTs [Paul and Chen, 2022], connecting to  
96 broader findings on shape versus texture bias in visual recognition [Geirhos et al., 2019]. While the  
97 impact of positional embeddings on robustness has been observed (particularly that models trained  
98 with PEs exhibit better robustness profiles than models trained without them) [Mao et al., 2021], the  
99 relationship between a model’s spatial organization strategy (whether anchored to absolute position  
100 or inferred from content) and its robustness to distributional shifts remains poorly understood.

###### 101 Our Contribution

102 We connect these lines of work by showing that positional embeddings are associated with a shift  
103 toward index-based spatial organization, and that this shift (rather than the specific encoding mech-  
104 anism) appears to be a dominant correlate of robustness. Using SSDC and controlled permutation  
105 interventions (RPT and RPI), we provide a geometric account of how positional information shapes  
106 internal representations and why it improves robustness.

###### 107 3 Preliminaries

###### 108 3.1 Vision Transformer Architecture and Positional Encodings

109 All models are Vision Transformers trained from scratch on ImageNet-100 (a subset of Imagenet-  
110 1K) [Deng et al., 2009], with approximately 22M parameters (details in Appendix A). Images are  
111 partitioned into fixed-size patches, projected into token embeddings, and processed by a stack of  
112 self-attention and feedforward layers.

113 Since self-attention is permutation invariant, positional encodings are required to inject spatial  
114 information. We consider three commonly used PE schemes, all adapted to 2D grids:

115 **Learned Absolute Positional Embeddings (APE):** learnable vectors added to token embeddings  
116 before the first transformer block, establishing a fixed index-to-location mapping.

117 **Sinusoidal Positional Embeddings (SPE):** fixed, deterministic encodings constructed from sinu-  
118 soidal functions applied independently along spatial axes and added to token embeddings.

119 **Rotary Positional Embeddings (RoPE):** position-dependent rotations applied to query and key  
120 vectors within each attention layer, introducing positional information multiplicatively.

121 These approaches differ in parameterization (learned vs. fixed) and integration (additive vs. multi-  
122 plicative), enabling comparison of how different positional signals shape internal representations.

###### 123 3.2 Index-Based and Content-Based Spatial Organization

124 We distinguish between two qualitatively distinct modes of spatial organization.

125 **Index-based spatial organization** refers to representations whose similarity structure depends  
126 systematically on token position. Tokens that are spatially proximate tend to have more similar  
127 representations by virtue of their indices, and this structure persists under disruptions to patch content.  
128 This definition is behavioral and does not assume explicit coordinate representations.

129 **Content-based spatial organization** refers to representations in which similarity is driven primarily  
130 by patch content. Spatial structure arises indirectly from natural image statistics and degrades under  
131 transformations that disrupt content or token ordering.

132 In practice, models may exhibit both behaviors; the key distinction is which signal dominates.

{3}------------------------------------------------

## 4 Methods

### 4.1 Residual Stream Geometry

At selected layers, we extract the residual stream as a matrix  $R \in \mathbb{R}^{T \times C}$ , where  $T$  is the number of tokens and  $C$  the embedding dimension. We compute pairwise cosine similarities between unit-normalized token representations to form a symmetric similarity matrix, averaged across the batch dimension.

### 4.2 Spatial Similarity Distance Correlation

Let  $S \in \mathbb{R}^{T \times T}$  denote the token similarity matrix, and let  $p_i \in \mathbb{N}^2$  denote the spatial coordinates of token  $i$ . Define the spatial distance matrix  $D$  by  $D_{ij} = \|p_i - p_j\|_1$ . We define SSDC as the Spearman rank correlation between similarity and negative spatial distance over all token pairs:

$$\text{SSDC} = \rho_{\text{Spearman}}(\{S_{ij}\}_{i < j}, \{-D_{ij}\}_{i < j}).$$

Higher SSDC values indicate that spatially proximate tokens tend to have more similar representations. We use Spearman rank correlation to remain agnostic to the precise functional form relating spatial distance and representational similarity.

Importantly, SSDC should be interpreted as a coarse proxy for spatial organization rather than a direct measurement of a specific mechanism. Absolute values may reflect multiple factors (e.g., data statistics, architectural biases), and therefore SSDC is primarily used comparatively (to track changes across depth and to measure sensitivity to controlled interventions).

### 4.3 Random Permutation at Inference (RPI)

To distinguish index-based from content-based organization, we randomly permute token order at inference while keeping positional indices fixed. This breaks the correspondence between token order and spatial location. Under this setup, spatial structure driven purely by patch content is expected to be disrupted, as spatially adjacent tokens no longer correspond to neighboring image patches. In contrast, if a model has learned representations that depend systematically on token indices via positional signals, some spatial structure may persist or be partially recoverable.

As a result, SSDC under RPI should be interpreted as an indicator of the extent to which spatial organization depends on token indices, rather than as a definitive separation between index-based and content-based mechanisms.

### 4.4 Random Permutation during Training (RPT)

Random Permutation Training (RPT) applies a fresh random permutation to the token sequence at every forward pass during training. At each batch, patch tokens are shuffled while positional embeddings remain fixed to their original indices, breaking the consistent mapping between token index and spatial location. This prevents the model from learning a stable index-based spatial organization despite the presence of positional signals.

### 4.5 Positional Embedding Magnitude Scaling

We scale positional embeddings at inference by a factor  $\alpha$ , replacing  $\mathbf{e}_i$  with  $\alpha \mathbf{e}_i$ . This provides a continuous intervention on positional signal strength without retraining. We apply this to APE and sinusoidal models; an equivalent scaling for RoPE is not directly defined due to its multiplicative formulation.

### 4.6 Fragility Score

We quantify robustness using the Fragility Score (FS):

$$\text{FS} = 1 - \frac{A_{\text{shift}}}{A_{\text{normal}}},$$

where  $A_{\text{normal}}$  and  $A_{\text{shift}}$  denote accuracy on clean and shifted data. Higher values indicate greater sensitivity to distributional shift.

{4}------------------------------------------------

![Figure 1: Evolution of SSDC across depth. (a) SSDC grows weakly and remains at a relatively high value across layers for untrained ablated models. (b) SSDC evolution for untrained ablated, trained ablated, and intact models. The trained ablated model shows a sharp increase in early layers, while the untrained ablated model shows a gradual increase. The intact model shows a sharp increase in early layers followed by a slight decrease and then a gradual increase.](de6e8b740c69dac308cce9edfec3eff4_img.jpg)

Figure 1 consists of two line plots. Plot (a) shows the SSDC (Spatial Similarity Coefficient) on the y-axis (ranging from 0.50 to 0.80) against the Layer number on the x-axis (ranging from 0 to 10). A single blue line represents the 'Untrained Ablated' model, showing a gradual increase in SSDC from approximately 0.58 at layer 0 to about 0.66 at layer 10. Plot (b) shows the SSDC on the y-axis (ranging from 0.40 to 0.70) against the Layer number on the x-axis (ranging from 0 to 10). Three lines are shown: 'Untrained Ablated' (blue), 'Ablated' (orange), and 'Intact' (green). The 'Untrained Ablated' line is the same as in (a). The 'Ablated' line starts at approximately 0.50, rises sharply to about 0.65 by layer 2, and then gradually increases to about 0.66 by layer 10. The 'Intact' line starts at approximately 0.50, rises sharply to about 0.68 by layer 2, and then gradually decreases to about 0.63 by layer 10. Shaded regions around the lines indicate variability across runs.

Figure 1: Evolution of SSDC across depth. (a) SSDC grows weakly and remains at a relatively high value across layers for untrained ablated models. (b) SSDC evolution for untrained ablated, trained ablated, and intact models. The trained ablated model shows a sharp increase in early layers, while the untrained ablated model shows a gradual increase. The intact model shows a sharp increase in early layers followed by a slight decrease and then a gradual increase.

(a) Evolution of SSDC across depth on untrained ablated models

(b) Evolution of SSDC across depth on untrained ablated models, trained ablated models, and intact (trained with APE) models

Figure 1: (a) SSDC grows weakly and remains at a relatively high value across layers, indicating static spatial correlations induced by architectural and data priors rather than learning. (b) While untrained ablated models exhibit relatively high but slowly varying SSDC consistent with static data and architectural priors, trained ablated models display a sharp increase in early layers, indicating the emergence of learned spatial structure despite the absence of explicit positional encoding.

## 175 5 Results

###### 176 5.1 Architectural Priors Induce Static Spatial Correlations at Initialization

177 **Experimental Setup:** We evaluate SSDC across all layers of untrained ablated models on the  
 178 Imagenet-100 dataset. Unless stated otherwise, all reported results are averaged over 4 random seeds.  
 179 Shaded regions in figures indicate variability across runs ( $\pm 1$  standard deviation).

180 **Results:** The untrained ablated model exhibits a substantial non-zero SSDC (approximately  
 181 0.57–0.64) with only a weak, gradual increase across depth (Figure 1a). This behavior is highly  
 182 consistent across runs and reflects static spatial correlations induced by architectural priors and the  
 183 inherent structure of natural images, rather than learned spatial reasoning.

184 Crucially, this baseline highlights that SSDC should not be interpreted as a standalone metric whose  
 185 absolute magnitude reflects the presence or strength of learned spatial organization. Even in the  
 186 absence of training, relatively high SSDC values emerge. Instead, the layer-wise dynamics of SSDC  
 187 (in particular, the rate and pattern of change across depth) are the informative signal. In contrast to the  
 188 shallow, nearly static progression observed here, trained models exhibit rapid and structured changes  
 189 in SSDC (e.g., sharp increases in early layers), indicating the emergence of learned spatial structure.

190 This establishes a static baseline, allowing us to distinguish genuinely learned spatial organization  
 191 from correlations that arise purely from architectural and data-driven effects.

###### 192 5.2 Emergence of Spatial Structure Without Positional Encoding

193 **Experimental Setup:** To investigate whether spatial structure can emerge in the absence of explicit  
 194 positional information, we evaluate SSDC across all layers of untrained ablated models, trained  
 195 ablated models, and trained intact (APE) models on the Imagenet-100 dataset.

196 **Results:** Figure 1b compares the layer-wise evolution of SSDC for an untrained ablated model,  
 197 a trained ablated model, and a trained model with positional embeddings. The untrained ablated  
 198 model exhibits relatively high SSDC (approximately 0.57–0.64) with only weak growth across depth,  
 199 reflecting static spatial correlations induced by architectural and data priors rather than learning.

200 In contrast, the trained ablated model shows a qualitatively different trajectory: starting from lower  
 201 SSDC, it exhibits a sharp increase in early layers followed by continued growth. This dynamic pattern  
 202 closely resembles that of the trained model with positional embeddings. The key distinction is not  
 203 absolute SSDC magnitude, but its evolution.

{5}------------------------------------------------

![Figure 2: SSDC under random permutation at inference (RPI). (a) Models with positional encodings: APE, RoPE, and Sinusoidal PEs. (b) Models without a stable positional reference frame: Ablated and RPT. Both plots show SSDC under RPI across 10 layers.](431b8889a0e7f676f0eef40859590349_img.jpg)

Figure 2 consists of two line plots, (a) and (b), showing the SSDC under random permutation at inference (RPI) across 10 layers for different models. Plot (a) is titled '(a) Models with positional encodings' and shows three models: APE (blue line), RoPE (orange line), and Sinusoidal PEs (green line). The y-axis is 'SSDC under RPI' ranging from -0.1 to 0.6. The x-axis is 'Layer' ranging from 0 to 10. APE and Sinusoidal PEs show a sharp increase in SSDC at layer 1, peaking around 0.5 and 0.6 respectively, and then gradually decreasing. RoPE shows a more gradual increase, reaching about 0.35 by layer 10. Plot (b) is titled '(b) Models without a stable positional reference frame' and shows two models: Ablated (blue line) and RPT (orange line). The y-axis is 'SSDC under RPI' ranging from -0.100 to 0.100. The x-axis is 'Layer' ranging from 0 to 10. Both models show a collapse to near-zero SSDC across all layers, with values staying very close to 0.0.

Figure 2: SSDC under random permutation at inference (RPI). (a) Models with positional encodings: APE, RoPE, and Sinusoidal PEs. (b) Models without a stable positional reference frame: Ablated and RPT. Both plots show SSDC under RPI across 10 layers.

(a) **Models with positional encodings.** APE, Sinusoidal PEs, and RoPE models exhibit substantial SSDC recovery under RPI, indicating spatial organization anchored to token indices. In contrast, models lacking a consistent positional mapping collapse to near-zero SSDC, revealing a purely content-based spatial organization.

(b) **Models without a stable positional reference frame.** Ablated and RPT models collapse to near-zero SSDC across all layers under RPI, indicating that their spatial structure is entirely content-driven and does not survive token permutation.

Figure 2: **SSDC under random permutation at inference (RPI).** RPI disrupts the correspondence between token content and spatial position. Only models that anchor spatial structure to token indices exhibit SSDC recovery after permutation. In contrast, models lacking a consistent positional mapping collapse to near-zero SSDC, revealing a purely content-based spatial organization.

204 These results indicate that non-trivial spatial structure emerges during training even without positional  
205 embeddings. This is consistent with the non-trivial performance of ablated models and prior evidence  
206 that transformers can implicitly recover positional information.

207 We emphasize that this emergent structure is not equivalent to that induced by positional embed-  
208 dings. Rather, this establishes that spatial organization can arise without explicit positional signals,  
209 motivating a more precise characterization of its underlying mechanism in the next section.

###### 210 5.3 Disentangling Index-Based and Content-Based Spatial Organization

211 **Experimental Setup:** To distinguish between index-based and content-based spatial organization,  
212 we evaluate SSDC across all layers under a *Random Permutation at Inference* (RPI) intervention.  
213 Concretely, patch tokens are randomly permuted before being processed by the transformer, while  
214 positional embedding indices (when present) remain fixed to their original spatial locations. This  
215 operation disrupts the correspondence between token content and spatial position, while preserving  
216 any mapping between token indices and positional embeddings.

217 Under this setup, any spatial structure that arises purely from patch content is destroyed, as spatially  
218 adjacent tokens no longer correspond to neighboring image patches. In contrast, if a model has  
219 learned to anchor its representations to absolute token indices via positional embeddings, spatial  
220 structure can be re-established through the fixed positional signal. As a result, *SSDC recovery under*  
221 *RPI* serves as a probe for index-based spatial organization: models that rely on absolute positional  
222 information exhibit non-trivial SSDC despite permutation, whereas models that rely on content-based  
223 cues collapse to near-zero SSDC.

224 We evaluate this behavior across models trained with learned absolute positional embeddings (APE),  
225 sinusoidal encodings, rotary embeddings (RoPE), no positional embeddings (ablated), and under  
226 Random Permutation Training (RPT).

227 **Results:** Models trained without positional embeddings exhibit a complete collapse of SSDC under  
228 RPI across all layers, suggesting that their spatial structure is predominantly content-driven under this  
229 probe. Despite exhibiting non-trivial SSDC in the unpermuted setting (Section 5.2), this structure  
230 does not survive disruption of patch content, indicating that it is not anchored to token indices.

231 In contrast, all models trained with positional embeddings show substantial SSDC recovery under  
232 RPI, indicating representations that are more consistent with index-anchored spatial organization.  
233 However, the nature of this recovery differs across encoding schemes. For APE and sinusoidal

{6}------------------------------------------------

![Figure 3: Robustness to distributional shifts. Two line plots showing fragility scores for different model variants under Gaussian Blur and JPEG Compression perturbations.](4086a572c080354982c11f1de4d6921d_img.jpg)

Figure 3 consists of two line plots, (a) and (b), showing fragility scores for five model variants: APE, RoPE, SPE, Ablated, and RPT. Both plots include error bars representing uncertainty.

(a) Gaussian Blur ( $\sigma = 2.5$ ). The y-axis is 'Gaussian Blur Fragility Score' ranging from 0.15 to 0.30. The x-axis is 'Model Condition'. The data points are approximately: APE (0.19), RoPE (0.15), SPE (0.21), Ablated (0.30), and RPT (0.24).

(b) JPEG Compression (quality = 5). The y-axis is 'JPEG Fragility Score' ranging from 0.3 to 0.6. The x-axis is 'Model Condition'. The data points are approximately: APE (0.44), RoPE (0.29), SPE (0.44), Ablated (0.64), and RPT (0.63).

Figure 3: Robustness to distributional shifts. Two line plots showing fragility scores for different model variants under Gaussian Blur and JPEG Compression perturbations.

(a) **Gaussian Blur** ( $\sigma = 2.5$ ). Fragility scores under a mild perturbation that removes high-frequency detail while largely preserving global spatial structure. Differences between models are present but compressed, reflecting the weaker disruption of content-based cues.

(b) **JPEG Compression** (quality = 5). Fragility scores under a strong content-disrupting transformation. Models with positional encodings exhibit substantially lower fragility than ablated and RPT models, with RoPE achieving the lowest fragility overall.

Figure 3: **Robustness to distributional shifts.** Fragility scores across model variants under two perturbation regimes. The gap between models with and without a stable positional reference frame is most pronounced under strong content disruption (JPEG), while remaining consistent but attenuated under milder perturbations (Gaussian blur).

234 embeddings, SSDC exhibits a rapid increase in early layers following permutation, reaching a peak  
235 within the first few layers before stabilizing or slightly decreasing. This behavior suggests that spatial  
236 structure is injected early in the network via additive positional signals.

237 RoPE models display a qualitatively different trajectory: SSDC increases more gradually and  
238 continues to grow with depth, without a pronounced early-layer peak. This indicates that positional  
239 information is integrated progressively throughout the network, consistent with its multiplicative  
240 incorporation into attention mechanisms. A similar depth-wise pattern is observed in the unpermuted  
241 setting (Appendix C.1).

242 RPT models, despite having positional embeddings present, fail to exhibit meaningful SSDC recovery  
243 under RPI, behaving similarly to fully ablated models. This suggests that the mere presence of  
244 positional embeddings is insufficient; a consistent mapping between token indices and spatial locations  
245 during training appears necessary for index-based spatial organization to emerge.

246 Taken together, these results establish that positional embeddings are associated with a shift from  
247 content-based to index-based spatial organization, and that this shift depends critically on the stability  
248 of the positional reference frame rather than on the architectural presence of positional signals alone.

###### 249 5.4 Robustness to Content-Preserving and Content-Disrupting Perturbations

250 **Experimental Setup:** To evaluate how spatial organization strategy influences robustness, we  
251 measure performance under distribution shifts that perturb image content while preserving global  
252 structure. We consider two transformations:

253 **JPEG Compression:** We apply aggressive compression (quality = 5), introducing blocking artifacts  
254 that strongly disrupt local texture statistics while preserving coarse spatial layout. This provides a  
255 targeted probe of reliance on content-based cues.

256 **Gaussian Blur:** We apply Gaussian blur with standard deviation  $\sigma = 2.5$ , attenuating high-frequency  
257 detail while preserving low-frequency structure. This constitutes a milder perturbation than JPEG.

258 For each model, we compute the *Fragility Score* (FS), defined as the relative drop in accuracy under  
259 each transformation. We also report the raw accuracy of each model condition in Appendix D.

260 We include **Random Permutation Training (RPT)** as a critical control, allowing us to distinguish  
261 between the mere presence of positional signals and the emergence of a consistent positional reference  
262 frame.

{7}------------------------------------------------

263 We emphasize that these robustness results are limited to content-disrupting perturbations (e.g.,  
264 compression artifacts and blur) and do not necessarily generalize to other forms of distribution shift.

265 **Results:** Under JPEG compression, models with positional encodings exhibit substantially lower  
266 fragility (APE and sinusoidal:  $\sim 0.43$ , RoPE:  $\sim 0.30$ ) than ablated and RPT models ( $\sim 0.66$ ). This large  
267 gap indicates that robustness to severe content degradation is strongly influenced by the presence of a  
268 stable positional reference frame. Within PE-based models, RoPE consistently achieves lower fragility,  
269 suggesting a secondary effect of the encoding mechanism. We speculate that RoPE’s progressive  
270 depth-wise accumulation of spatial structure may keep later layers more spatially grounded than the  
271 early-layer injection characteristic of additive encodings.

272 Under Gaussian blur, the same ordering is preserved but differences are attenuated (RoPE:  $\sim 0.15$ ,  
273 APE:  $\sim 0.17$ – $0.20$ , sinusoidal:  $\sim 0.22$ , RPT:  $\sim 0.25$ , ablated:  $\sim 0.30$ ). Because blur preserves global  
274 structure, it provides a weaker test of reliance on content-based cues, reducing the separation between  
275 models.

276 Taken together, these results support a two-level interpretation: (1) the emergence of a stable  
277 positional reference frame appears to be a dominant factor associated with robustness, and (2) the  
278 specific encoding mechanism introduces secondary variation, with RoPE exhibiting consistently  
279 lower fragility. Crucially, the poor robustness of RPT models shows that the mere presence of  
280 positional embeddings is insufficient: robustness appears to rely on learning a consistent mapping  
281 between token indices and spatial locations. This provides evidence for a relationship between the  
282 spatial organization patterns identified earlier and downstream robustness.

###### 283 5.5 Linking Index-Based Spatial Organization to Robustness via Positional Scaling

284 **Experimental Setup:** To probe the relationship between spatial organization and robustness, we  
285 require a controlled intervention that selectively disrupts index-based spatial structure while preserving  
286 the rest of the model. We achieve this by scaling the magnitude of learned absolute positional  
287 embeddings (APE) at inference time by a factor  $\alpha \in [0, 1]$ , without retraining.

288 While this intervention operates on positional embeddings, our goal is not to study positional signal  
289 strength per se, but to use it as a mechanism to continuously degrade the model’s *index-based spatial*  
290 *organization*. To measure the integrity of this organization, we evaluate Spatial Similarity Distance  
291 Correlation (SSDC) under Random Permutation at Inference (RPI), as introduced in Section 5.3.  
292 Under RPI, any recovered spatial structure must be anchored to token indices rather than content. We  
293 therefore interpret SSDC recovery as a proxy for the presence of index-based spatial organization.  
294 Importantly, SSDC recovery approaching zero does not imply content-based spatial structure; it  
295 indicates that the positional signal is too weak to sustain index-based organization.

296 To summarize this behavior compactly, we define:

$$\Delta \text{SSDC} = \text{SSDC}_{\text{layer } 1} - \text{SSDC}_{\text{layer } 0},$$

297 which captures the immediate recovery of spatial structure after the first encoder block under RPI.  
298 Thus,  $\Delta \text{SSDC}$  serves as a measure of index-based spatial organization.

299 We jointly analyze  $\Delta \text{SSDC}$  and the Fragility Score (FS) across varying  $\alpha$ . For clarity, we report  
300 representative magnitudes illustrating distinct regimes, with the full results provided in Appendix B.1  
301 (and Appendix B.2 for Sinusoidal PEs).

| $\alpha$ | $\Delta \text{SSDC}$ (RPI) |  | Fragility Score |  |
|-|-|-|-|-|
|  | Mean | Std | Mean | Std |
| 1.0 | 0.4725 | 0.0228 | 0.4338 | 0.0127 |
| 0.8 | 0.3125 | 0.0259 | 0.4780 | 0.0146 |
| 0.7 | 0.1845 | 0.0342 | 0.5145 | 0.0145 |
| 0.5 | 0.0475 | 0.0083 | 0.5975 | 0.0202 |
| 0.4 | 0.0000 | 0.0000 | 0.6272 | 0.0189 |

Table 1: Effect of positional embedding magnitude  $\alpha$  on index-based spatial organization and  
robustness.  $\Delta \text{SSDC}$  captures the recovery of index-based spatial structure after the first encoder block.  
As  $\alpha$  decreases,  $\Delta \text{SSDC}$  collapses, indicating the breakdown of index-based spatial organization,  
while fragility increases sharply in the same regime before plateauing once spatial structure is lost.

{8}------------------------------------------------

302 **Results:** We observe a clear correspondence between the degradation of index-based spatial organization  
303 and the loss of robustness.

304 At high magnitudes ( $\alpha \geq 0.9$ ), models exhibit strong SSDC recovery ( $\Delta\text{SSDC} \approx 0.37\text{--}0.47$ ),  
305 indicating intact index-based spatial organization. In this regime, fragility remains relatively low and  
306 stable ( $\text{FS} \approx 0.44\text{--}0.46$ ), suggesting that robustness is preserved when spatial structure is intact.

307 As  $\alpha$  decreases into an intermediate regime ( $0.8 \geq \alpha \geq 0.5$ ), SSDC recovery drops sharply  
308 ( $\Delta\text{SSDC} \approx 0.30 \rightarrow 0.02$ ), reflecting the progressive breakdown of index-based spatial organization.  
309 This degradation is accompanied by a pronounced increase in fragility ( $\text{FS} \approx 0.48 \rightarrow 0.63$ ). Notably,  
310 the most significant increases in fragility occur precisely where SSDC recovery is actively decreasing,  
311 indicating that robustness degradation is strongly correlated with the loss of spatial structure.

312 Below a critical threshold ( $\alpha \leq 0.4$ ), SSDC recovery collapses to zero ( $\Delta\text{SSDC} \approx 0$ ), indicating that  
313 index-based spatial organization is no longer recoverable under permutation. In this regime, fragility  
314 continues to increase, but only marginally ( $\text{FS} \approx 0.65 \rightarrow 0.685$ ). This suggests that once spatial  
315 organization is fully disrupted, further degradation in robustness is no longer correlated with changes  
316 in spatial structure, but instead reflects secondary effects such as reduced representational quality or  
317 distribution mismatch induced by scaling.

318 A complementary effect is observed at high magnitudes: when index-based spatial organization  
319 is already fully intact, small reductions in  $\alpha$  have limited impact on fragility. Together, these  
320 observations reveal three regimes: (1) a stable regime with intact spatial organization and low  
321 fragility, (2) a transition regime where spatial structure degrades and fragility increases sharply, and  
322 (3) a collapsed regime where spatial organization is absent and fragility plateaus.

323 Overall, these results provide evidence that robustness may be driven in part by the presence of  
324 index-based spatial organization. Positional scaling serves only as a means of intervention; the  
325 observed changes in robustness track the degradation of spatial structure rather than the magnitude of  
326 the positional signal itself.

###### 327 6 Limitations

328 The findings reported here are based on ViT-S models trained from scratch on ImageNet-100, and it  
329 remains an open question whether the observed relationships between positional encoding, index-  
330 based spatial organization, and robustness generalize to larger architectures, pre-trained models, or  
331 models fine-tuned from large-scale checkpoints. The robustness evaluation is specifically scoped  
332 to content-disrupting perturbations (JPEG compression and Gaussian blur); we make no claims  
333 about spatial perturbations, adversarial shifts, or semantic distribution changes, and these may  
334 involve different mechanisms. SSDC is used as a coarse proxy for spatial organization rather than  
335 a direct measurement of a specific representational mechanism, and its interpretation depends on  
336 the comparative and intervention-based framing established in Section 5.1. Finally, the positional  
337 scaling experiment (Section 5.5) conflates spatial organization degradation with changes in raw  
338 positional signal magnitude, and while the three-regime structure is consistent with a mediating role  
339 for index-based organization, alternative pathways cannot be fully excluded.

## 340 7 Conclusion

341 We studied how positional encodings shape spatial organization in Vision Transformers and its  
342 relationship to robustness under content-disrupting perturbations. Using SSDC and permutation-  
343 based interventions, we found that spatial structure emerges even without positional encodings, but  
344 remains content-driven and collapses under token permutation. Models with positional encodings  
345 exhibit representations more consistent with index-anchored spatial organization. Across experiments,  
346 robustness under content-disrupting shifts is closely associated with a stable positional reference  
347 frame rather than the mere presence of positional embeddings — evidenced by RPT models and  
348 positional scaling, where robustness degrades alongside the breakdown of index-anchored spatial  
349 structure. Differences between encoding schemes persist but appear secondary. Overall, our results  
350 suggest positional encodings contribute to robustness by supporting a stable positional reference  
351 frame, though we emphasize this conclusion is based on intervention-based evidence and identifies a  
352 strong relationship rather than a fully isolated causal mechanism.

{9}------------------------------------------------

## References

- 353  
354 Srinadh Bhojanapalli, Ayan Chakrabarti, Daniel Glasner, Daliang Li, Thomas Unterthiner, and  
355 Andreas Veit. Understanding robustness of transformers for image classification. pages 10211–  
356 10221, 10 2021. doi: 10.1109/ICCV48922.2021.01007.
- 357 Xiangxiang Chu, Zhi Tian, Bo Zhang, Xinlong Wang, and Chunhua Shen. Conditional positional  
358 encodings for vision transformers. In *The Eleventh International Conference on Learning Repre-*  
359 *sentations*, 2023. URL <https://openreview.net/forum?id=3KWnuT-R1bh>.
- 360 Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Imagenet: A large-scale hier-  
361 archical image database. In *2009 IEEE Conference on Computer Vision and Pattern Recognition*,  
362 pages 248–255, 2009. doi: 10.1109/CVPR.2009.5206848.
- 363 Yihe Dong, Jean-Baptiste Cordonnier, and Andreas Loukas. Attention is not all you need: pure  
364 attention loses rank doubly exponentially with depth. In Marina Meila and Tong Zhang, edi-  
365 tors, *Proceedings of the 38th International Conference on Machine Learning*, volume 139 of  
366 *Proceedings of Machine Learning Research*, pages 2793–2803. PMLR, 18–24 Jul 2021. URL  
367 <https://proceedings.mlr.press/v139/dong21a.html>.
- 368 Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas  
369 Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit,  
370 and Neil Houlsby. An image is worth 16x16 words: Transformers for image recognition at scale.  
371 In *International Conference on Learning Representations*, 2021. URL <https://openreview.net/forum?id=YicbFdNTTy>.
- 372  
373 Stéphane d’Ascoli, Hugo Touvron, Matthew L Leavitt, Ari S Morcos, Giulio Biroli, and Levent  
374 Sagun. Convit: improving vision transformers with soft convolutional inductive biases\*. *Journal*  
375 *of Statistical Mechanics: Theory and Experiment*, 2022(11):114005, nov 2022. doi: 10.1088/1742-5468/ac9830. URL <https://doi.org/10.1088/1742-5468/ac9830>.
- 376  
377 Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda  
378 Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, Dawn Drain, Deep Ganguli, As-  
379 zack Hatfield-Dodds, Danny Hernandez, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal  
380 Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, and Chris  
381 Olah. A mathematical framework for transformer circuits. *Transformer Circuits Thread*, 2021.  
382 <https://transformer-circuits.pub/2021/framework/index.html>.
- 383  
384 Robert Geirhos, Patricia Rubisch, Claudio Michaelis, Matthias Bethge, Felix A. Wichmann, and  
385 Wieland Brendel. Imagenet-trained CNNs are biased towards texture; increasing shape bias  
386 improves accuracy and robustness. In *International Conference on Learning Representations*,  
387 2019. URL <https://openreview.net/forum?id=Bygh9j09KX>.
- 388  
389 Byeongho Heo, Song Park, Dongyoon Han, and Sangdoon Yun. Rotary position embedding for  
390 vision transformer. In *Computer Vision – ECCV 2024: 18th European Conference, Milan, Italy*,  
391 *September 29–October 4, 2024, Proceedings, Part X*, page 289–305. Berlin, Heidelberg, 2024.  
392 Springer-Verlag. ISBN 978-3-031-72683-5. doi: 10.1007/978-3-031-72684-2\_17. URL [https://doi.org/10.1007/978-3-031-72684-2\\_17](https://doi.org/10.1007/978-3-031-72684-2_17).
- 393  
394 Md Amirul Islam\*, Sen Jia\*, and Neil D. B. Bruce. How much position information do convolutional  
395 neural networks encode? In *International Conference on Learning Representations*, 2020. URL  
396 <https://openreview.net/forum?id=rJeB36NKvB>.
- 397  
398 Amirhossein Kazemnejad, Inkit Padhi, Karthikeyan Natesan, Payel Das, and Siva Reddy. The impact  
399 of positional encoding on length generalization in transformers. In *Thirty-seventh Conference on*  
400 *Neural Information Processing Systems*, 2023. URL <https://openreview.net/forum?id=Drr12gcj2l>.
- 401  
402 Goro Kobayashi, Tatsuki Kuribayashi, Sho Yokoi, and Kentaro Inui. Incorporating Residual and  
403 Normalization Layers into Analysis of Masked Language Models. In Marie-Francine Moens,  
404 Xuanjing Huang, Lucia Specia, and Scott Wen-tau Yih, editors, *Proceedings of the 2021 Con-*  
405 *ference on Empirical Methods in Natural Language Processing*, pages 4547–4568. Association  
406 for Computational Linguistics, November 2021. doi: 10.18653/v1/2021.emnlp-main.373. URL  
407 <https://aclanthology.org/2021.emnlp-main.373/>.

 Rest of paper (reference and Appendix) is removed.