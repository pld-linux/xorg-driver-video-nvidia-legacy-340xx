#
# Conditional build:
%bcond_without	dist_kernel	# without distribution kernel
%bcond_without	up		# without up packages
%bcond_without	smp		# without smp packages
%bcond_without	kernel		# without kernel packages
%bcond_without	incall		# include all tarballs
%bcond_without	userspace	# don't build userspace programs
%bcond_with	verbose		# verbose build (V=1)
#
%define		no_install_post_strip 1
#
%define		_nv_ver		1.0
%define		_nv_rel		9746
%define		_min_x11	6.7.0
%define		_rel		1
#
%define		need_x86	0
%define		need_x8664	0
%if %{with incall}
%define		need_x86	1
%define		need_x8664	1
%else
%ifarch %{ix86}
%define		need_x86	1
%endif
%ifarch %{x8664}
%define		need_x8664	1
%endif
%endif
#
Summary:	Linux Drivers for nVidia TNT/TNT2/GeForce/Quadro Chips
Summary(pl):	Sterowniki do kart graficznych nVidia TNT/TNT2/GeForce/Quadro
Name:		xorg-driver-video-nvidia
Version:	%{_nv_ver}.%{_nv_rel}
Release:	%{_rel}
License:	nVidia Binary
Group:		X11
%if %{need_x86}
Source0:	http://us.download.nvidia.com/XFree86/Linux-x86/%{_nv_ver}-%{_nv_rel}/NVIDIA-Linux-x86-%{_nv_ver}-%{_nv_rel}-pkg1.run
# Source0-md5:	cf0cdbd9099a6df028de429044e7f4da
%endif
%if %{need_x8664}
Source1:	http://us.download.nvidia.com/XFree86/Linux-x86_64/%{_nv_ver}-%{_nv_rel}/NVIDIA-Linux-x86_64-%{_nv_ver}-%{_nv_rel}-pkg2.run
# Source1-md5:	c0afc66e1c21a9a54ba6719b8edd3166
%endif
Source2:	%{name}-xinitrc.sh
Patch0:		X11-driver-nvidia-GL.patch
Patch1:		X11-driver-nvidia-desktop.patch
URL:		http://www.nvidia.com/object/linux.html
%if %{with kernel}
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.7}
%endif
BuildRequires:	%{kgcc_package}
BuildRequires:	rpmbuild(macros) >= 1.330
BuildRequires:	sed >= 4.0
BuildConflicts:	XFree86-nvidia
Requires:	xorg-xserver-server
Provides:	OpenGL = 1.5
Provides:	OpenGL-GLX
Provides:	xorg-xserver-modules-libglx
Obsoletes:	Mesa
Obsoletes:	X11-OpenGL-core < 1:7.0.0
Obsoletes:	X11-OpenGL-libGL < 1:7.0.0
Obsoletes:	XFree86-OpenGL-core < 1:7.0.0
Obsoletes:	XFree86-OpenGL-libGL < 1:7.0.0
Obsoletes:	XFree86-driver-nvidia
Obsoletes:	XFree86-nvidia
Conflicts:	XFree86-OpenGL-devel <= 4.2.0-3
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLcore.so.1

%description
This driver set adds improved 2D functionality to the Xorg/XFree86 X
server as well as high performance OpenGL acceleration, AGP support,
support for most flat panels, and 2D multiple monitor support.

Hardware: nVidia TNT, TNT2, GeForce, or Quadro based graphics
accelerator. The nVidia NV1 and RIVA 128/128ZX chips are supported in
the base Xorg/XFree86 install and are not supported by this driver
set.

%description -l pl
Usprawnione sterowniki dla kart graficznych nVidia do serwera
Xorg/XFree86, daj±ce wysokowydajn± akceleracjê OpenGL, obs³ugê AGP i
wielu monitorów 2D.

Obs³uguj± karty nVidia TNT/TNT2/GeForce/Quadro do serwera
Xorg/XFree86; Karty nVidia NV1 i Riva 128/128ZX s± obs³ugiwane przez
sterownik nv z pakietów Xorg/XFree8 - NIE s± obs³ugiwane przez ten
pakiet.

%package devel
Summary:	OpenGL for X11R6 development (only gl?.h)
Summary(pl):	Pliki nag³ówkowe OpenGL dla systemu X11R6 (tylko gl?.h)
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	OpenGL-GLX-devel
Provides:	OpenGL-devel = 1.5
Provides:	OpenGL-devel-base
Obsoletes:	OpenGL-devel-base
Obsoletes:	XFree86-driver-nvidia-devel
Conflicts:	XFree86-OpenGL-devel < 4.3.99.902-0.3

%description devel
Base headers (only gl?.h) for OpenGL for X11R6 for nvidia drivers.

%description devel -l pl
Podstawowe pliki nag³ówkowe (tylko gl?.h) OpenGL dla systemu X11R6 dla
sterowników nvidii.

%package progs
Summary:	Tools for advanced control of nVidia graphic cards
Summary(pl):	Narzêdzia do zarz±dzania kartami graficznymi nVidia
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Obsoletes:	XFree86-driver-nvidia-progs

%description progs
Tools for advanced control of nVidia graphic cards.

%description progs -l pl
Narzêdzia do zarz±dzania kartami graficznymi nVidia.

%package -n kernel%{_alt_kernel}-video-nvidia
Summary:	nVidia kernel module for nVidia Architecture support
Summary(de):	Das nVidia-Kern-Modul für die nVidia-Architektur-Unterstützung
Summary(pl):	Modu³ j±dra dla obs³ugi kart graficznych nVidia
Version:	%{_nv_ver}.%{_nv_rel}
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.7.7-10
%{?with_dist_kernel:%requires_releq_kernel_up}
Provides:	X11-driver-nvidia(kernel)
Obsoletes:	XFree86-nvidia-kernel

%description -n kernel%{_alt_kernel}-video-nvidia
nVidia Architecture support for Linux kernel.

%description -n kernel%{_alt_kernel}-video-nvidia -l de
Die nVidia-Architektur-Unterstützung für den Linux-Kern.

%description -n kernel%{_alt_kernel}-video-nvidia -l pl
Obs³uga architektury nVidia dla j±dra Linuksa. Pakiet wymagany przez
sterownik nVidii dla Xorg/XFree86.

%package -n kernel%{_alt_kernel}-smp-video-nvidia
Summary:	nVidia kernel module for nVidia Architecture support
Summary(de):	Das nVidia-Kern-Modul für die nVidia-Architektur-Unterstützung
Summary(pl):	Modu³ j±dra dla obs³ugi kart graficznych nVidia
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.7.7-10
%{?with_dist_kernel:%requires_releq_kernel_smp}
Provides:	X11-driver-nvidia(kernel)
Obsoletes:	XFree86-nvidia-kernel

%description -n kernel%{_alt_kernel}-smp-video-nvidia
nVidia Architecture support for Linux kernel SMP.

%description -n kernel%{_alt_kernel}-smp-video-nvidia -l de
Die nVidia-Architektur-Unterstützung für den Linux-Kern SMP.

%description -n kernel%{_alt_kernel}-smp-video-nvidia -l pl
Obs³uga architektury nVidia dla j±dra Linuksa SMP. Pakiet wymagany
przez sterownik nVidii dla Xorg/XFree86.

%prep
cd %{_builddir}
rm -rf NVIDIA-Linux-x86*-%{_nv_ver}-%{_nv_rel}-pkg*
%ifarch %{ix86}
/bin/sh %{SOURCE0} --extract-only
%setup -qDT -n NVIDIA-Linux-x86-%{_nv_ver}-%{_nv_rel}-pkg1
%else
/bin/sh %{SOURCE1} --extract-only
%setup -qDT -n NVIDIA-Linux-x86_64-%{_nv_ver}-%{_nv_rel}-pkg2
%endif
%patch0 -p1
%patch1 -p1
echo 'EXTRA_CFLAGS += -Wno-pointer-arith -Wno-sign-compare -Wno-unused' >> usr/src/nv/Makefile.kbuild

%build
%if %{with kernel}
cd usr/src/nv/
ln -sf Makefile.kbuild Makefile
cat >> Makefile <<'EOF'

$(obj)/nv-kernel.o: $(src)/nv-kernel.o.bin
	cp $< $@
EOF
mv nv-kernel.o{,.bin}
%build_kernel_modules -m nvidia
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with userspace}
install -d $RPM_BUILD_ROOT%{_libdir}/xorg/modules/{drivers,extensions} \
	$RPM_BUILD_ROOT{%{_includedir}/GL,%{_libdir},%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},/etc/X11/xinit/xinitrc.d}

install usr/bin/nvidia-{settings,xconfig,bug-report.sh} $RPM_BUILD_ROOT%{_bindir}
install usr/share/man/man1/nvidia-{settings,xconfig}.* $RPM_BUILD_ROOT%{_mandir}/man1
install usr/share/applications/nvidia-settings.desktop $RPM_BUILD_ROOT%{_desktopdir}
install usr/share/pixmaps/nvidia-settings.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d/nvidia-settings.sh

for f in \
	usr/lib/tls/libnvidia-tls.so.%{version}		\
	usr/lib/libnvidia-cfg.so.%{version}		\
	usr/lib/libGL{,core}.so.%{version}		\
	usr/X11R6/lib/libXvMCNVIDIA.so.%{version}	\
	usr/X11R6/lib/libXvMCNVIDIA.a			\
; do
	install $f $RPM_BUILD_ROOT%{_libdir}
done

install usr/X11R6/lib/modules/extensions/libglx.so.%{version} \
	$RPM_BUILD_ROOT%{_libdir}/xorg/modules/extensions
install usr/X11R6/lib/modules/drivers/nvidia_drv.so \
	$RPM_BUILD_ROOT%{_libdir}/xorg/modules/drivers
install usr/X11R6/lib/modules/libnvidia-wfb.so.%{version} \
	$RPM_BUILD_ROOT%{_libdir}/xorg/modules

install usr/include/GL/*.h $RPM_BUILD_ROOT%{_includedir}/GL

ln -sf libglx.so.%{version} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/extensions/libglx.so
ln -sf libXvMCNVIDIA.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libXvMCNVIDIA.so
ln -sf libXvMCNVIDIA.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libXvMCNVIDIA_dynamic.so.1

# OpenGL ABI for Linux compatibility
ln -sf libGL.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libGL.so.1
ln -sf libGL.so.1 $RPM_BUILD_ROOT%{_libdir}/libGL.so
%endif

%if %{with kernel}
%install_kernel_modules -m usr/src/nv/nvidia -d misc
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
cat << EOF

 *******************************************************
 *                                                     *
 *  NOTE:                                              *
 *  You must install:                                  *
 *  kernel(24)(-smp)-video-nvidia-%{version}             *
 *  for this driver to work                            *
 *                                                     *
 *******************************************************

EOF

%postun	-p /sbin/ldconfig

%post	-n kernel%{_alt_kernel}-video-nvidia
%depmod %{_kernel_ver}

%postun	-n kernel%{_alt_kernel}-video-nvidia
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-smp-video-nvidia
%depmod %{_kernel_ver}smp

%postun	-n kernel%{_alt_kernel}-smp-video-nvidia
%depmod %{_kernel_ver}smp

%if %{with userspace}
%files
%defattr(644,root,root,755)
%doc LICENSE
%doc usr/share/doc/{README.txt,NVIDIA_Changelog,XF86Config.sample,html}
# OpenGL ABI for Linux compatibility
%attr(755,root,root) %{_libdir}/libGL.so
%attr(755,root,root) %{_libdir}/libGL.so.1
#
%attr(755,root,root) %{_libdir}/libGL.so.*.*
%attr(755,root,root) %{_libdir}/libGLcore.so.*.*
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA.so.*.*
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA_dynamic.so.1
%attr(755,root,root) %{_libdir}/libnvidia-cfg.so.*.*.*
%attr(755,root,root) %{_libdir}/libnvidia-tls.so.*.*.*
%attr(755,root,root) %{_libdir}/xorg/modules/libnvidia-wfb.so.*.*.*
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/nvidia_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libglx.so*
%endif

%if %{with kernel}
%if %{with up} || %{without dist_kernel}
%files -n kernel%{_alt_kernel}-video-nvidia
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/*.ko*
%endif

%if %{with smp} && %{with dist_kernel}
%files -n kernel%{_alt_kernel}-smp-video-nvidia
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/*.ko*
%endif
%endif

%if %{with userspace}
%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA.so
%{_includedir}/GL/*.h
# -static
%{_libdir}/libXvMCNVIDIA.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nvidia-settings
%attr(755,root,root) %{_bindir}/nvidia-xconfig
%attr(755,root,root) %{_bindir}/nvidia-bug-report.sh
%attr(755,root,root) /etc/X11/xinit/xinitrc.d/*.sh
%{_desktopdir}/nvidia-settings.desktop
%{_mandir}/man1/nvidia-*
%{_pixmapsdir}/nvidia-settings.png
%endif
