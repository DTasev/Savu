Plugin API 
===================
Information on specific functions, classes, and methods.
 
savu
------------------------------------------------------------

.. toctree::
   api_plugin/savu.tomo_recon
   api_plugin/savu.version


savu.core
------------------------------------------------------------

.. toctree::
   api_plugin/savu.core.plugin_runner
   api_plugin/savu.core.transport_setup
   api_plugin/savu.core.utils
   api_plugin/savu.core.basic_plugin_runner
   api_plugin/savu.core.checkpointing


savu.core.transports
------------------------------------------------------------

.. toctree::
   api_plugin/savu.core.transports.base_transport
   api_plugin/savu.core.transports.basic_transport
   api_plugin/savu.core.transports.hdf5_transport
   api_plugin/savu.core.transports.dosna_transport


savu.data
------------------------------------------------------------

.. toctree::
   api_plugin/savu.data.chunking
   api_plugin/savu.data.experiment_collection
   api_plugin/savu.data.plugin_list
   api_plugin/savu.data.framework_citations
   api_plugin/savu.data.meta_data


savu.data.data_structures
------------------------------------------------------------

.. toctree::
   api_plugin/savu.data.data_structures.data
   api_plugin/savu.data.data_structures.data_add_ons
   api_plugin/savu.data.data_structures.data_create
   api_plugin/savu.data.data_structures.data_notes
   api_plugin/savu.data.data_structures.plugin_data
   api_plugin/savu.data.data_structures.preview
   api_plugin/savu.data.data_structures.utils


savu.data.data_structures.data_types
------------------------------------------------------------

.. toctree::
   api_plugin/savu.data.data_structures.data_types.data_plus_darks_and_flats
   api_plugin/savu.data.data_structures.data_types.base_type
   api_plugin/savu.data.data_structures.data_types.image_data
   api_plugin/savu.data.data_structures.data_types.map_3dto4d_h5
   api_plugin/savu.data.data_structures.data_types.mrc
   api_plugin/savu.data.data_structures.data_types.replicate
   api_plugin/savu.data.data_structures.data_types.stitch_data


savu.data.transport_data
------------------------------------------------------------

.. toctree::
   api_plugin/savu.data.transport_data.base_transport_data
   api_plugin/savu.data.transport_data.hdf5_transport_data
   api_plugin/savu.data.transport_data.basic_transport_data
   api_plugin/savu.data.transport_data.dosna_transport_data
   api_plugin/savu.data.transport_data.slice_lists


savu.plugins
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.docstring_parser
   api_plugin/savu.plugins.plugin
   api_plugin/savu.plugins.plugin_datasets
   api_plugin/savu.plugins.plugin_datasets_notes
   api_plugin/savu.plugins.utils


savu.plugins.absorption_corrections
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.absorption_corrections.base_absorption_correction
   api_plugin/savu.plugins.absorption_corrections.mc_near_absorption_correction


savu.plugins.alignment
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.alignment.projection_shift
   api_plugin/savu.plugins.alignment.projection_vertical_alignment
   api_plugin/savu.plugins.alignment.sinogram_alignment
   api_plugin/savu.plugins.alignment.sinogram_clean


savu.plugins.analysis
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.analysis.stxm_analysis
   api_plugin/savu.plugins.analysis.base_analysis
   api_plugin/savu.plugins.analysis.histogram
   api_plugin/savu.plugins.analysis.stats


savu.plugins.azimuthal_integrators
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.azimuthal_integrators.base_azimuthal_integrator
   api_plugin/savu.plugins.azimuthal_integrators.pyfai_azimuthal_integrator_with_bragg_filter
   api_plugin/savu.plugins.azimuthal_integrators.pyfai_azimuthal_integrator
   api_plugin/savu.plugins.azimuthal_integrators.pyfai_azimuthal_integrator_separate


savu.plugins.basic_operations
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.basic_operations.basic_operations
   api_plugin/savu.plugins.basic_operations.no_process_plugin
   api_plugin/savu.plugins.basic_operations.arithmetic_operations
   api_plugin/savu.plugins.basic_operations.data_rescale
   api_plugin/savu.plugins.basic_operations.get_data_statistics


savu.plugins.centering
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.centering.vo_centering
   api_plugin/savu.plugins.centering.vo_centering_iterative
   api_plugin/savu.plugins.centering.vo_centering_gpu


savu.plugins.component_analysis
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.component_analysis.base_component_analysis
   api_plugin/savu.plugins.component_analysis.ica
   api_plugin/savu.plugins.component_analysis.pca


savu.plugins.corrections
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.corrections.base_correction
   api_plugin/savu.plugins.corrections.dark_flat_field_correction
   api_plugin/savu.plugins.corrections.monitor_correction
   api_plugin/savu.plugins.corrections.convert_360_180_sinogram
   api_plugin/savu.plugins.corrections.time_based_correction
   api_plugin/savu.plugins.corrections.camera_rot_correction
   api_plugin/savu.plugins.corrections.distortion_correction
   api_plugin/savu.plugins.corrections.monitor_correction_nd
   api_plugin/savu.plugins.corrections.subpixel_shift
   api_plugin/savu.plugins.corrections.time_based_plus_drift_correction
   api_plugin/savu.plugins.corrections.timeseries_field_corrections
   api_plugin/savu.plugins.corrections.xrd_absorption_approximation
   api_plugin/savu.plugins.corrections.distortion_correction_deprecated


savu.plugins.developing
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.developing.testing_sino_align


savu.plugins.driver
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.driver.all_cpus_plugin
   api_plugin/savu.plugins.driver.cpu_plugin
   api_plugin/savu.plugins.driver.gpu_plugin
   api_plugin/savu.plugins.driver.plugin_driver
   api_plugin/savu.plugins.driver.base_driver
   api_plugin/savu.plugins.driver.basic_driver
   api_plugin/savu.plugins.driver.multi_threaded_plugin
   api_plugin/savu.plugins.driver.iterative_plugin
   api_plugin/savu.plugins.driver.single_node_multi_threaded_plugin


savu.plugins.filters
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.filters.denoise_bregman_filter
   api_plugin/savu.plugins.filters.band_pass
   api_plugin/savu.plugins.filters.base_filter
   api_plugin/savu.plugins.filters.paganin_filter
   api_plugin/savu.plugins.filters.ccpi_denoising_cpu
   api_plugin/savu.plugins.filters.ccpi_denoising_gpu
   api_plugin/savu.plugins.filters.list_to_projections
   api_plugin/savu.plugins.filters.dials_find_spots
   api_plugin/savu.plugins.filters.find_peaks
   api_plugin/savu.plugins.filters.median_filter
   api_plugin/savu.plugins.filters.dezinger
   api_plugin/savu.plugins.filters.poly_background_estimator
   api_plugin/savu.plugins.filters.dezinger_simple
   api_plugin/savu.plugins.filters.dezinger_sinogram
   api_plugin/savu.plugins.filters.pymca
   api_plugin/savu.plugins.filters.quantisation_filter
   api_plugin/savu.plugins.filters.spectrum_crop
   api_plugin/savu.plugins.filters.strip_background
   api_plugin/savu.plugins.filters.threshold_filter
   api_plugin/savu.plugins.filters.hilbert_filter
   api_plugin/savu.plugins.filters.image_interpolation
   api_plugin/savu.plugins.filters.umpa
   api_plugin/savu.plugins.filters.fresnel_filter


savu.plugins.fitters
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.fitters.base_fitter
   api_plugin/savu.plugins.fitters.ral_fit
   api_plugin/savu.plugins.fitters.reproduce_fit
   api_plugin/savu.plugins.fitters.simple_fit


savu.plugins.fluo_fitters
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.fluo_fitters.base_fluo_fitter
   api_plugin/savu.plugins.fluo_fitters.fastxrf_fitting
   api_plugin/savu.plugins.fluo_fitters.simple_fit_xrf


savu.plugins.kinematics
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.kinematics.stage_motion


savu.plugins.loaders
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.loaders.base_loader
   api_plugin/savu.plugins.loaders.random_hdf5_loader
   api_plugin/savu.plugins.loaders.hdf5_template_loader
   api_plugin/savu.plugins.loaders.stitch_data_template_loader
   api_plugin/savu.plugins.loaders.multi_savu_loader
   api_plugin/savu.plugins.loaders.image_template_loader
   api_plugin/savu.plugins.loaders.savu_nexus_loader
   api_plugin/savu.plugins.loaders.yaml_converter


savu.plugins.loaders.full_field_loaders
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.loaders.full_field_loaders.image_loader
   api_plugin/savu.plugins.loaders.full_field_loaders.fake_nxtomo_loader
   api_plugin/savu.plugins.loaders.full_field_loaders.multi_nxtomo_loader
   api_plugin/savu.plugins.loaders.full_field_loaders.mrc_loader
   api_plugin/savu.plugins.loaders.full_field_loaders.nxtomo_loader
   api_plugin/savu.plugins.loaders.full_field_loaders.dxchange_loader
   api_plugin/savu.plugins.loaders.full_field_loaders.random_3d_tomo_loader


savu.plugins.loaders.mapping_loaders
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.loaders.mapping_loaders.base_multi_modal_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.mm_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.nxfluo_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.nxmonitor_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.nxptycho_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.nxstxm_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.nxxrd_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.txm_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.p2r_fly_scan_detector_loader


savu.plugins.loaders.mapping_loaders.i08_loaders
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.loaders.mapping_loaders.i08_loaders.i08_fluo_loader


savu.plugins.loaders.mapping_loaders.i13_loaders
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.loaders.mapping_loaders.i13_loaders.i13_stxm_monitor_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.i13_loaders.i13_fluo_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.i13_loaders.i13_ptycho_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.i13_loaders.i13_speckle_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.i13_loaders.i13_stxm_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.i13_loaders.i13_stxm_xrf_loader


savu.plugins.loaders.mapping_loaders.i14_loaders
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.loaders.mapping_loaders.i14_loaders.i14_fluo_loader


savu.plugins.loaders.mapping_loaders.i18_loaders
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.loaders.mapping_loaders.i18_loaders.base_i18_multi_modal_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.i18_loaders.i18_xrd_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.i18_loaders.i18_fluo_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.i18_loaders.i18_mm_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.i18_loaders.i18_monitor_loader
   api_plugin/savu.plugins.loaders.mapping_loaders.i18_loaders.i18_stxm_loader


savu.plugins.loaders.mapping_loaders.i22_loaders
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.loaders.mapping_loaders.i22_loaders.i22_tomo_loader


savu.plugins.loaders.templates
------------------------------------------------------------

.. toctree::


savu.plugins.loaders.templates.i18_templates
------------------------------------------------------------

.. toctree::


savu.plugins.loaders.templates.malcolm_templates
------------------------------------------------------------

.. toctree::


savu.plugins.loaders.templates.nexus_templates
------------------------------------------------------------

.. toctree::


savu.plugins.loaders.utils
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.loaders.utils.yaml_utils
   api_plugin/savu.plugins.loaders.utils.mrc_header


savu.plugins.missing_data
------------------------------------------------------------

.. toctree::


savu.plugins.ptychography
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.ptychography.base_ptycho
   api_plugin/savu.plugins.ptychography.ptypy_batch
   api_plugin/savu.plugins.ptychography.dummy_ptycho
   api_plugin/savu.plugins.ptychography.ptypy_compact


savu.plugins.reconstructions
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.reconstructions.tomopy_recon
   api_plugin/savu.plugins.reconstructions.base_recon
   api_plugin/savu.plugins.reconstructions.ccpi_cgls_recon
   api_plugin/savu.plugins.reconstructions.scikitimage_filter_back_projection
   api_plugin/savu.plugins.reconstructions.scikitimage_sart
   api_plugin/savu.plugins.reconstructions.simple_recon
   api_plugin/savu.plugins.reconstructions.visual_hulls_recon
   api_plugin/savu.plugins.reconstructions.tomobar_recon_cpu
   api_plugin/savu.plugins.reconstructions.tomobar_recon
   api_plugin/savu.plugins.reconstructions.tomobar_recon_3D


savu.plugins.reconstructions.astra_recons
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.reconstructions.astra_recons.astra_recon_cpu
   api_plugin/savu.plugins.reconstructions.astra_recons.astra_recon_gpu
   api_plugin/savu.plugins.reconstructions.astra_recons.base_astra_recon


savu.plugins.reshape
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.reshape.data_removal
   api_plugin/savu.plugins.reshape.downsample_filter
   api_plugin/savu.plugins.reshape.mipmap


savu.plugins.ring_removal
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.ring_removal.ccpi_ring_artefact_filter
   api_plugin/savu.plugins.ring_removal.raven_filter
   api_plugin/savu.plugins.ring_removal.remove_all_rings
   api_plugin/savu.plugins.ring_removal.remove_large_rings
   api_plugin/savu.plugins.ring_removal.ring_removal_normalization
   api_plugin/savu.plugins.ring_removal.ring_removal_regularization
   api_plugin/savu.plugins.ring_removal.ring_removal_filtering
   api_plugin/savu.plugins.ring_removal.ring_removal_waveletfft
   api_plugin/savu.plugins.ring_removal.ring_removal_fitting
   api_plugin/savu.plugins.ring_removal.ring_removal_sorting
   api_plugin/savu.plugins.ring_removal.remove_unresponsive_and_fluctuating_rings


savu.plugins.savers
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.savers.base_saver
   api_plugin/savu.plugins.savers.hdf5_saver
   api_plugin/savu.plugins.savers.tiff_saver
   api_plugin/savu.plugins.savers.base_image_saver
   api_plugin/savu.plugins.savers.edf_saver
   api_plugin/savu.plugins.savers.image_saver
   api_plugin/savu.plugins.savers.xrf_saver


savu.plugins.savers.utils
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.savers.utils.hdf5_utils


savu.plugins.segmentation
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.segmentation.gmm_segment3D
   api_plugin/savu.plugins.segmentation.geo_distance
   api_plugin/savu.plugins.segmentation.mask_evolve
   api_plugin/savu.plugins.segmentation.mask_initialiser
   api_plugin/savu.plugins.segmentation.morph_snakes
   api_plugin/savu.plugins.segmentation.morph_snakes3D
   api_plugin/savu.plugins.segmentation.thresh_segm


savu.plugins.segmentation.i23segmentation
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.segmentation.i23segmentation.final_segment_i23
   api_plugin/savu.plugins.segmentation.i23segmentation.i23_segment
   api_plugin/savu.plugins.segmentation.i23segmentation.i23_segment3D


savu.plugins.segmentation.morphological_operations
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.segmentation.morphological_operations.morph_proc


savu.plugins.visualisation
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.visualisation.ortho_slice


savu.plugins.stats
------------------------------------------------------------

.. toctree::
   api_plugin/savu.plugins.stats.min_and_max


