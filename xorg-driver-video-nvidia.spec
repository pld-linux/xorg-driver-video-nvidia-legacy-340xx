#
# Conditional build:
%bcond_without	dist_kernel	# without distribution kernel
%bcond_without	smp		# without smp packages
%bcond_without	kernel		# without kernel packages
%bcond_with	verbose		# verbose build (V=1)
%bcond_with	tls		# install libraries with tls support
#
%define		_nv_ver		1.0
%define		_nv_rel		6111
%define		_min_x11	6.7.0
%define		_rel		5
#
Summary:	Linux Drivers for nVidia TNT/TNT2/GeForce/Quadro Chips
Summary(pl):	Sterowniki do kart graficznych nVidia TNT/TNT2/GeForce/Quadro
Name:		X11-driver-nvidia
Version:	%{_nv_ver}.%{_nv_rel}
Release:	%{_rel}
License:	nVidia Binary
Vendor:		nVidia Corp.
Group:		X11/XFree86
# why not pkg0!?
Source0:	http://download.nvidia.com/XFree86/Linux-x86/%{_nv_ver}-%{_nv_rel}/NVIDIA-Linux-x86-%{_nv_ver}-%{_nv_rel}-pkg1.run
# Source0-md5:	51e83be46f83c52102ccb8995b54f4e2
# Source0-size:	8167999
Source1:	http://download.nvidia.com/XFree86/Linux-x86_64/%{_nv_ver}-%{_nv_rel}/NVIDIA-Linux-x86_64-%{_nv_ver}-%{_nv_rel}-pkg2.run
# Source1-md5:	6c7b0c8b3ce5c34186e0c80042e6d046
# Source1-size:	7333486
Patch0:		%{name}-gcc34.patch
Patch1:		%{name}-GL.patch
Patch2:		%{name}-pci_x_class.patch
Patch3:		%{name}-enable-pci.patch 
Patch4:		%{name}-power-suspend.patch
URL:		http://www.nvidia.com/object/linux.html
BuildConflicts:	XFree86-nvidia
BuildRequires:	grep
%{?with_dist_kernel:BuildRequires:	kernel-module-build >= 2.6.7}
BuildRequires:	%{kgcc_package}
BuildRequires:	rpmbuild(macros) >= 1.153
BuildRequires:	sed >= 4.0
BuildRequires:	textutils
#BuildRequires:	X11-devel >= %{_min_x11}	# disabled for now
Requires:	X11-Xserver
Requires:	X11-libs >= %{_min_x11}
Requires:	X11-modules >= %{_min_x11}
%{?with_tls:Requires:	glibc(tls)}
Provides:	X11-OpenGL-core
Provides:	X11-OpenGL-libGL
Provides:	XFree86-OpenGL-core
Provides:	XFree86-OpenGL-libGL
Obsoletes:	Mesa
Obsoletes:	X11-OpenGL-core
Obsoletes:	X11-OpenGL-libGL
Obsoletes:	XFree86-OpenGL-core
Obsoletes:	XFree86-OpenGL-libGL
Obsoletes:	XFree86-driver-nvidia
Obsoletes:	XFree86-nvidia
Conflicts:	XFree86-OpenGL-devel <= 4.2.0-3
ExclusiveArch:	%{ix86} amd64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLcore.so.1
%define		_prefix		/usr/X11R6
%ifarch amd64
%define		_libdir32	%{_prefix}/lib
%endif

%description
This driver set adds improved 2D functionality to the XFree86 4.0 X
server as well as high performance OpenGL acceleration, AGP support,
support for most flat panels, and 2D multiple monitor support.

Hardware: nVidia TNT, TNT2, GeForce, or Quadro based graphics
accelerator. The nVidia NV1 and RIVA 128/128ZX chips are supported in
the base XFree86 4.0 install and are not supported by this driver set.

Software: Linux kernel >= 2.2.12, XFree86 >= 4.0.

%description -l pl
Usprawnione sterowniki dla kart graficznych nVidia do serwera XFree86
4.0, daj±ce wysokowydajn± akceleracjê OpenGL, obs³ugê AGP i wielu
monitorów 2D.

Obs³uguj± karty nVidia TNT/TNT2/GeForce/Quadro do serwera XFree86 4.0;
Karty nVidia NV1 i Riva 128/128ZX s± obs³ugiwane przez sterownik nv z
pakietów XFree86 - NIE s± obs³ugiwane przez ten pakiet.

%package devel
Summary:	OpenGL for X11R6 development (only gl?.h)
Summary(pl):	Pliki nag³ówkowe OpenGL dla systemu X11R6 (tylko gl?.h)
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
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
Obsoletes:	XFree86-driver-nvidia-progs
Requires:	%{name} = %{version}-%{release}

%description progs
Tools for advanced control of nVidia graphic cards.

%description progs -l pl
Narzêdzia do zarz±dzania kartami graficznymi nVidia.

%package -n kernel-video-nvidia
Summary:	nVidia kernel module for nVidia Architecture support
Summary(de):	Das nVidia-Kern-Modul für die nVidia-Architektur-Unterstützung
Summary(pl):	Modu³ j±dra dla obs³ugi kart graficznych nVidia
Version:	%{_nv_ver}.%{_nv_rel}
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
PreReq:		modutils >= 2.3.18-2
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.7.7-10
%{?with_dist_kernel:%requires_releq_kernel_up}
Provides:	X11-driver-nvidia(kernel)
Obsoletes:	XFree86-nvidia-kernel

%description -n kernel-video-nvidia
nVidia Architecture support for Linux kernel.

%description -n kernel-video-nvidia -l de
Die nVidia-Architektur-Unterstützung für den Linux-Kern.

%description -n kernel-video-nvidia -l pl
Obs³uga architektury nVidia dla j±dra Linuksa. Pakiet wymagany przez
sterownik nVidii dla XFree86 4.

%package -n kernel-smp-video-nvidia
Summary:	nVidia kernel module for nVidia Architecture support
Summary(de):	Das nVidia-Kern-Modul für die nVidia-Architektur-Unterstützung
Summary(pl):	Modu³ j±dra dla obs³ugi kart graficznych nVidia
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
PreReq:		modutils >= 2.3.18-2
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.7.7-10
%{?with_dist_kernel:%requires_releq_kernel_smp}
Provides:	X11-driver-nvidia(kernel)
Obsoletes:	XFree86-nvidia-kernel

%description -n kernel-smp-video-nvidia
nVidia Architecture support for Linux kernel SMP.

%description -n kernel-smp-video-nvidia -l de
Die nVidia-Architektur-Unterstützung für den Linux-Kern SMP.

%description -n kernel-smp-video-nvidia -l pl
Obs³uga architektury nVidia dla j±dra Linuksa SMP. Pakiet wymagany
przez sterownik nVidii dla XFree86 4.

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
%patch2 -p1
%patch3 -p1
%patch4 -p1
sed -i 's:-Wpointer-arith::' usr/src/nv/Makefile.kbuild

%build
%if %{with kernel}
cd usr/src/nv/
ln -sf Makefile.kbuild Makefile
for cfg in %{?with_dist_kernel:%{?with_smp:smp} up}%{!?with_dist_kernel:nondist}; do
	if [ ! -r "%{_kernelsrcdir}/config-$cfg" ]; then
		exit 1
	fi
	rm -rf include
	install -d include/{linux,config}
	ln -sf %{_kernelsrcdir}/config-$cfg .config
	ln -sf %{_kernelsrcdir}/include/linux/autoconf-$cfg.h include/linux/autoconf.h
	ln -sf %{_kernelsrcdir}/include/asm-%{_target_base_arch} include/asm
	touch include/config/MARKER
	%{__make} -C %{_kernelsrcdir} clean \
		RCS_FIND_IGNORE="-name '*.ko' -o -name nv-kernel.o -o" \
		M=$PWD O=$PWD \
		%{?with_verbose:V=1}
	%{__make} -C %{_kernelsrcdir} modules \
		CC="%{__cc}" CPP="%{__cpp}" \
		M=$PWD O=$PWD \
		%{?with_verbose:V=1}
	mv nvidia.ko nvidia-$cfg.ko
done
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/modules/{drivers,extensions} \
	$RPM_BUILD_ROOT{/usr/include/GL,/usr/%{_lib},%{_bindir}}

ln -sf $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_prefix}/../lib

install usr/bin/nvidia-settings $RPM_BUILD_ROOT%{_bindir}
install usr/lib%{?with_tls:/tls}/libnvidia-tls.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install usr/lib/libGL{,core}.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install usr/X11R6/lib/modules/extensions/libglx.so.%{version} \
	$RPM_BUILD_ROOT%{_libdir}/modules/extensions
%ifarch amd64
# support for running 32-bit OpenGL applications on 64-bit AMD64 Linux installations
#install -d $RPM_BUILD_ROOT%{_libdir32}
#install usr/lib32%{?with_tls:/tls}/libnvidia-tls.so.%{version} $RPM_BUILD_ROOT%{_libdir32}
#install usr/lib32/libGL{,core}.so.%{version} $RPM_BUILD_ROOT%{_libdir32}
%endif

install usr/X11R6/lib/modules/drivers/nvidia_drv.o $RPM_BUILD_ROOT%{_libdir}/modules/drivers
install usr/X11R6/lib/libXvMCNVIDIA.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install usr/include/GL/*.h	$RPM_BUILD_ROOT/usr/include/GL
#install usr/bin/nvidia-settings $RPM_BUILD_ROOT%{_bindir}

ln -sf libGL.so.1 $RPM_BUILD_ROOT%{_libdir}/libGL.so
ln -sf libglx.so.%{version} $RPM_BUILD_ROOT%{_libdir}/modules/extensions/libglx.so
ln -sf libXvMCNVIDIA.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libXvMCNVIDIA.so

# OpenGL ABI for Linux compatibility
ln -sf %{_libdir}/libGL.so.1 $RPM_BUILD_ROOT/usr/%{_lib}/libGL.so.1
ln -sf %{_libdir}/libGL.so $RPM_BUILD_ROOT/usr/%{_lib}/libGL.so

cd usr/src/nv/
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/misc
install nvidia-%{?with_dist_kernel:up}%{!?with_dist_kernel:nondist}.ko \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/nvidia.ko
%if %{with smp} && %{with dist_kernel}
install nvidia-smp.ko \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/nvidia.ko
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

%post	-n kernel-video-nvidia
%depmod %{_kernel_ver}

%postun	-n kernel-video-nvidia
%depmod %{_kernel_ver}

%post	-n kernel-smp-video-nvidia
%depmod %{_kernel_ver}smp

%postun	-n kernel-smp-video-nvidia
%depmod %{_kernel_ver}smp

%files
%defattr(644,root,root,755)
%doc LICENSE
%doc usr/share/doc/{README,NVIDIA_Changelog,XF86Config.sample}
%lang(de) %doc usr/share/doc/README.DE
%attr(755,root,root) %{_libdir}/libGL.so.*.*
%attr(755,root,root) %{_libdir}/libGL.so
%attr(755,root,root) %{_libdir}/libGLcore.so.*.*
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA.so.*.*
%attr(755,root,root) %{_libdir}/libnvidia-tls.so.*.*.*
%ifarch amd64
# support for running 32-bit OpenGL applications on 64-bit AMD64 Linux installations
#dir %{_libdir32}
#attr(755,root,root) %{_libdir32}/libGL.so.*.*
#attr(755,root,root) %{_libdir32}/libGLcore.so.*.*
#attr(755,root,root) %{_libdir32}/libXvMCNVIDIA.so.*.*
#attr(755,root,root) %{_libdir32}/libnvidia-tls.so.*.*.*
%endif
%attr(755,root,root) /usr/%{_lib}/libGL.so.1
%attr(755,root,root) /usr/%{_lib}/libGL.so
%attr(755,root,root) %{_libdir}/modules/extensions/libglx.so*
%attr(755,root,root) %{_libdir}/modules/drivers/nvidia_drv.o

%if %{with kernel}
%files -n kernel-video-nvidia
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/*.ko*

%if %{with smp} && %{with dist_kernel}
%files -n kernel-smp-video-nvidia
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/*.ko*
%endif
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA.so
/usr/include/GL/*.h
# -static
%{_libdir}/libXvMCNVIDIA.a

%files progs
%defattr(755,root,root,755)
%{_bindir}/nvidia-settings
