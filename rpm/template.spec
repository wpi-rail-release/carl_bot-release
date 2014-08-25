Name:           ros-indigo-carl-bringup
Version:        0.0.3
Release:        0%{?dist}
Summary:        ROS carl_bringup package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/carl_bringup
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-carl-description
Requires:       ros-indigo-carl-dynamixel
Requires:       ros-indigo-carl-teleop
Requires:       ros-indigo-m4atx-battery-monitor
Requires:       ros-indigo-openni2-launch
Requires:       ros-indigo-ros-ethernet-rmp
Requires:       ros-indigo-urg-node
Requires:       ros-indigo-wpi-jaco-wrapper
BuildRequires:  ros-indigo-catkin

%description
CARL Bringup Launch Scripts

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Aug 25 2014 Russell Toris <rctoris@wpi.edu> - 0.0.3-0
- Autogenerated by Bloom

* Mon Aug 18 2014 Russell Toris <rctoris@wpi.edu> - 0.0.2-0
- Autogenerated by Bloom

* Fri Aug 15 2014 Russell Toris <rctoris@wpi.edu> - 0.0.1-0
- Autogenerated by Bloom

