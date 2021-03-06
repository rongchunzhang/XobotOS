{
  'includes': [
    'target_defaults.gypi',
  ],
  'defines!': [
    'SK_BUILD_FOR_MAC',
  ],
  'targets': [
    {
      'target_name': 'iOSSampleApp',
      'type': 'executable',
      'mac_bundle' : 1,
      'include_dirs' : [
        '../src/core', # needed to get SkConcaveToTriangle, maybe this should be moved to include dir?
        '../gm',       # SampleGM.cpp pulls gm.h
        '../include/pipe', # To pull in SkGPipe.h for pipe reader/writer
      ],
      'sources': [
        # gm files needed for SampleGM.cpp
        '../gm/bitmapfilters.cpp',
        '../gm/blurs.cpp',
        '../gm/complexclip.cpp',
        '../gm/filltypes.cpp',
        '../gm/gm.h',
        '../gm/gradients.cpp',
        '../gm/nocolorbleed.cpp',
        '../gm/points.cpp',
        '../gm/poly2poly.cpp',
        '../gm/shadertext.cpp',
        '../gm/shadows.cpp',
        '../gm/shapes.cpp',
        '../gm/tilemodes.cpp',
        '../gm/xfermodes.cpp',

        '../samplecode/ClockFaceView.cpp',
        '../samplecode/OverView.cpp',
        '../samplecode/Sample2PtRadial.cpp',
        '../samplecode/SampleAll.cpp',
        '../samplecode/SampleAnimator.cpp',
        '../samplecode/SampleApp.cpp',
        '../samplecode/SampleArc.cpp',
        '../samplecode/SampleAvoid.cpp',
        '../samplecode/SampleBigBlur.cpp',
        '../samplecode/SampleBigGradient.cpp',
        '../samplecode/SampleBitmapRect.cpp',
        '../samplecode/SampleBlur.cpp',
        '../samplecode/SampleCamera.cpp',
        '../samplecode/SampleCircle.cpp',
        '../samplecode/SampleCode.h',
        '../samplecode/SampleColorFilter.cpp',
        '../samplecode/SampleComplexClip.cpp',
        '../samplecode/SampleConcavePaths.cpp',
        '../samplecode/SampleCull.cpp',
        '../samplecode/SampleDecode.cpp',
        '../samplecode/SampleDegenerateTwoPtRadials.cpp',
        '../samplecode/SampleDither.cpp',
        '../samplecode/SampleDitherBitmap.cpp',
        '../samplecode/SampleDrawBitmap.cpp',
        '../samplecode/SampleDrawLooper.cpp',
        '../samplecode/SampleEffects.cpp',
        '../samplecode/SampleEmboss.cpp',
        '../samplecode/SampleEncode.cpp',
        '../samplecode/SampleExtractAlpha.cpp',
        '../samplecode/SampleFillType.cpp',
        '../samplecode/SampleFilter.cpp',
        '../samplecode/SampleFilter2.cpp',
        '../samplecode/SampleFontCache.cpp',
        '../samplecode/SampleFontScalerTest.cpp',
        '../samplecode/SampleFuzz.cpp',
        '../samplecode/SampleGM.cpp',
        '../samplecode/SampleGradients.cpp',
        '../samplecode/SampleHairline.cpp',
        '../samplecode/SampleImage.cpp',
        '../samplecode/SampleImageDir.cpp',
        '../samplecode/SampleLayerMask.cpp',
        '../samplecode/SampleLayers.cpp',
        '../samplecode/SampleLCD.cpp',
        '../samplecode/SampleLineClipper.cpp',
        '../samplecode/SampleLines.cpp',
        '../samplecode/SampleMeasure.cpp',
        '../samplecode/SampleMipMap.cpp',
        '../samplecode/SampleMovie.cpp',
        '../samplecode/SampleNinePatch.cpp',
        '../samplecode/SampleOvalTest.cpp',
        '../samplecode/SampleOverflow.cpp',
        '../samplecode/SamplePageFlip.cpp',
        '../samplecode/SamplePatch.cpp',
        '../samplecode/SamplePath.cpp',
        '../samplecode/SamplePathClip.cpp',
        '../samplecode/SamplePathEffects.cpp',
        '../samplecode/SamplePicture.cpp',
        '../samplecode/SamplePoints.cpp',
        '../samplecode/SamplePolyToPoly.cpp',
        '../samplecode/SampleAARects.cpp',
        '../samplecode/SampleRegion.cpp',
        '../samplecode/SampleRepeatTile.cpp',
        '../samplecode/SampleShaders.cpp',
        '../samplecode/SampleShaderText.cpp',
        '../samplecode/SampleShapes.cpp',
        '../samplecode/SampleSkLayer.cpp',
        '../samplecode/SampleSlides.cpp',
        '../samplecode/SampleStrokePath.cpp',
        '../samplecode/SampleStrokeText.cpp',
        '../samplecode/SampleTests.cpp',
        '../samplecode/SampleText.cpp',
        '../samplecode/SampleTextAlpha.cpp',
        '../samplecode/SampleTextBox.cpp',
        '../samplecode/SampleTextEffects.cpp',
        '../samplecode/SampleTextOnPath.cpp',
        '../samplecode/SampleTextureDomain.cpp',
        '../samplecode/SampleTiling.cpp',
        '../samplecode/SampleTinyBitmap.cpp',
        '../samplecode/SampleTriangles.cpp',
        '../samplecode/SampleTypeface.cpp',
        '../samplecode/SampleUnitMapper.cpp',
        '../samplecode/SampleVertices.cpp',
        '../samplecode/SampleXfermodes.cpp',
        '../samplecode/SampleXfermodesBlur.cpp',
        
        # Dependencies for the pipe code in SampleApp
        '../src/pipe/SkGPipeRead.cpp',
        '../src/pipe/SkGPipeWrite.cpp',
        
        # DrawingBoard
        '../experimental/DrawingBoard/SkColorPalette.h',
        '../experimental/DrawingBoard/SkColorPalette.cpp',
        '../experimental/DrawingBoard/SkNetPipeController.h',
        '../experimental/DrawingBoard/SkNetPipeController.cpp',
        '../experimental/DrawingBoard/SampleDrawingClient.cpp',
        '../experimental/DrawingBoard/SampleDrawingServer.cpp',
    
        # Networking
        '../experimental/Networking/SampleNetPipeReader.cpp',
        '../experimental/Networking/SkSockets.cpp',
        '../experimental/Networking/SkSockets.h',
        
        # Transition
        '../src/utils/SkInterpolator.cpp',
        '../include/utils/SkInterpolator.h',
        '../samplecode/TransitionView.cpp',
      ],
      'sources!': [
        '../samplecode/SampleSkLayer.cpp', #relies on SkMatrix44 which doesn't compile
        '../samplecode/SampleTests.cpp',   #includes unknown file SkShaderExtras.h
        '../samplecode/SampleWarp.cpp',
        '../samplecode/SampleFontCache.cpp',
      ],
      'dependencies': [
        'core.gyp:core',
        'effects.gyp:effects',
        'images.gyp:images',
        'views.gyp:views',
        'utils.gyp:utils',
        'animator.gyp:animator',
        'xml.gyp:xml',
        'svg.gyp:svg',
        'experimental.gyp:experimental',
        'gpu.gyp:gr',
        'gpu.gyp:skgr',
        'pdf.gyp:pdf',
      ],
      'conditions' : [
       [ 'OS == "linux" or OS == "freebsd" or OS == "openbsd" or OS == "solaris"', {
         'sources!': [
            '../samplecode/SampleDecode.cpp',
         ],
        }],
        [ 'OS == "win"', {
          'sources!': [
            # require UNIX functions
            '../samplecode/SampleEncode.cpp',
            '../samplecode/SamplePageFlip.cpp',
          ],
        }],
        [ 'OS == "mac"', {
          'sources!': [
            '../samplecode/SampleDecode.cpp',
            '../src/gpu/mac/GrGLDefaultInterface_mac.cpp',
          ],
          'sources': [
            # Shared resources
            '../experimental/SkEventNotifier.h',
            '../experimental/SkEventNotifier.mm',
            '../experimental/iOSSampleApp/SkiOSSampleApp-Base.xcconfig',
            '../experimental/iOSSampleApp/SkiOSSampleApp-Debug.xcconfig',
            '../experimental/iOSSampleApp/SkiOSSampleApp-Release.xcconfig',
            '../experimental/iOSSampleApp/iOSSampleApp-Info.plist',
            '../experimental/iOSSampleApp/iOSSampleApp_Prefix.pch',
            '../experimental/iOSSampleApp/Shared/SkOptionListController.h',
            '../experimental/iOSSampleApp/Shared/SkOptionListController.mm',
            '../experimental/iOSSampleApp/Shared/SkUIRootViewController.h',
            '../experimental/iOSSampleApp/Shared/SkUIRootViewController.mm',
            '../experimental/iOSSampleApp/Shared/SkOptionsTableViewController.h',
            '../experimental/iOSSampleApp/Shared/SkOptionsTableViewController.mm',
            '../experimental/iOSSampleApp/Shared/SkUIView.h',
            '../experimental/iOSSampleApp/Shared/SkUIView.mm',
            '../experimental/iOSSampleApp/Shared/SkUIDetailViewController.h',
            '../experimental/iOSSampleApp/Shared/SkUIDetailViewController.mm',
            '../experimental/iOSSampleApp/Shared/main.m',
            
            # iPad
            '../experimental/iOSSampleApp/iPad/AppDelegate_iPad.h',
            '../experimental/iOSSampleApp/iPad/AppDelegate_iPad.mm',
            '../experimental/iOSSampleApp/iPad/SkUISplitViewController.h',
            '../experimental/iOSSampleApp/iPad/SkUISplitViewController.mm',
            '../experimental/iOSSampleApp/iPad/MainWindow_iPad.xib',
            
            # iPhone
            '../experimental/iOSSampleApp/iPhone/AppDelegate_iPhone.h',
            '../experimental/iOSSampleApp/iPhone/AppDelegate_iPhone.mm',
            '../experimental/iOSSampleApp/iPhone/SkUINavigationController.h',
            '../experimental/iOSSampleApp/iPhone/SkUINavigationController.mm',
            '../experimental/iOSSampleApp/iPhone/MainWindow_iPhone.xib',

            '../src/utils/ios/SkOSWindow_iOS.mm',
            '../src/utils/ios/SkImageDecoder_iOS.mm',
            '../src/utils/ios/SkStream_NSData.mm',
            '../src/utils/ios/SkOSFile_iOS.mm',

            '../include/utils/mac/SkCGUtils.h',
            '../src/utils/mac/SkCreateCGImageRef.cpp',
            '../experimental/iOSSampleApp/SkiOSSampleApp-Debug.xcconfig',
            '../experimental/iOSSampleApp/SkiOSSampleApp-Release.xcconfig',
          ],
          'link_settings': {
            'libraries': [
              '/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS4.3.sdk/System/Library/Frameworks/CoreFoundation.framework',
              '/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS4.3.sdk/System/Library/Frameworks/CoreGraphics.framework',
              '/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS4.3.sdk/System/Library/Frameworks/CoreText.framework',
              '/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS4.3.sdk/System/Library/Frameworks/UIKit.framework',
              '/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS4.3.sdk/System/Library/Frameworks/Foundation.framework',
              '/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS4.3.sdk/System/Library/Frameworks/QuartzCore.framework',
              '/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS4.3.sdk/System/Library/Frameworks/OpenGLES.framework',
            ],
            'libraries!': [
              #remove mac dependencies
              '$(SDKROOT)/System/Library/Frameworks/Cocoa.framework',
              '$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
              '$(SDKROOT)/System/Library/Frameworks/QuartzCore.framework',
              '$(SDKROOT)/System/Library/Frameworks/OpenGL.framework',
              '$(SDKROOT)/System/Library/Frameworks/ApplicationServices.framework',
            ],
          },
          'include_dirs' : [
            '../experimental/iOSSampleApp',
            '../experimental/iOSSampleApp/iPad',
            '../experimental/iOSSampleApp/iPhone',
            '../include/utils/ios',
            '../../include/gpu',
          ],
          #'xcode_settings' : {
          #  'INFOPLIST_FILE' : '../experimental/iOSSampleApp/iOSSampleApp-Info.plist',
          #  'ARCHS' : 'armv6 armv7',
          #  'IPHONEOS_DEPLOYMENT_TARGET' : '4.2',
          #  'SDKROOT' : 'iphoneos',
          #  'TARGETED_DEVICE_FAMILY' : '1,2',
          #  'USER_HEADER_SEARCH_PATHS' : '../../gpu/include/** ../../include/**',
          #  'CODE_SIGN_IDENTITY' : 'iPhone Developer',
          #  'GCC_PREPROCESSOR_DEFINITIONS' : 'SK_BUILD_FOR_IOS',
          #  'GCC_OPTIMIZATION_LEVEL' : '0',
          #},
          'xcode_config_file': '../experimental/iOSSampleApp/SkiOSSampleApp-Base.xcconfig',
          'mac_bundle_resources' : [
            '../experimental/iOSSampleApp/iPad/MainWindow_iPad.xib',
            '../experimental/iOSSampleApp/iPhone/MainWindow_iPhone.xib',
          ],
        }],

      ],
    },
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
