Name:           ros-indigo-carl-phidgets
Version:        0.0.27
Release:        0%{?dist}
Summary:        ROS carl_phidgets package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/carl_phidgets
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-libphidgets
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-libphidgets
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf

%description
ROS Support for the Phidgets Spatial 3/3/3 Devices for use with the CARL Robot

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Apr 22 2015 David Kent <davidkent@wpi.edu> - 0.0.27-0
- Autogenerated by Bloom

* Fri Apr 17 2015 David Kent <davidkent@wpi.edu> - 0.0.26-0
- Autogenerated by Bloom

* Fri Apr 10 2015 David Kent <davidkent@wpi.edu> - 0.0.25-0
- Autogenerated by Bloom

* Mon Apr 06 2015 David Kent <davidkent@wpi.edu> - 0.0.24-0
- Autogenerated by Bloom

* Fri Apr 03 2015 David Kent <davidkent@wpi.edu> - 0.0.23-0
- Autogenerated by Bloom

* Fri Apr 03 2015 David Kent <davidkent@wpi.edu> - 0.0.22-0
- Autogenerated by Bloom

* Tue Mar 31 2015 David Kent <davidkent@wpi.edu> - 0.0.21-0
- Autogenerated by Bloom

* Tue Mar 31 2015 David Kent <davidkent@wpi.edu> - 0.0.20-0
- Autogenerated by Bloom

* Fri Mar 27 2015 David Kent <davidkent@wpi.edu> - 0.0.19-0
- Autogenerated by Bloom

* Fri Mar 27 2015 David Kent <davidkent@wpi.edu> - 0.0.18-0
- Autogenerated by Bloom

* Tue Mar 24 2015 David Kent <davidkent@wpi.edu> - 0.0.17-0
- Autogenerated by Bloom

* Tue Feb 17 2015 David Kent <davidkent@wpi.edu> - 0.0.16-0
- Autogenerated by Bloom

* Tue Feb 10 2015 David Kent <davidkent@wpi.edu> - 0.0.15-0
- Autogenerated by Bloom

* Fri Feb 06 2015 David Kent <davidkent@wpi.edu> - 0.0.14-0
- Autogenerated by Bloom

* Wed Jan 21 2015 David Kent <davidkent@wpi.edu> - 0.0.13-0
- Autogenerated by Bloom

* Mon Jan 19 2015 David Kent <davidkent@wpi.edu> - 0.0.12-0
- Autogenerated by Bloom

