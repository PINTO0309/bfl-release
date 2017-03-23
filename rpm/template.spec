Name:           ros-lunar-bfl
Version:        0.7.0
Release:        0%{?dist}
Summary:        ROS bfl package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/bfl
Source0:        %{name}-%{version}.tar.gz

Requires:       cppunit-devel
Requires:       ros-lunar-catkin
Requires:       ros-lunar-ros
BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  ros-lunar-ros

%description
This package contains a recent version of the Bayesian Filtering Library (BFL),
distributed by the Orocos Project. For stability reasons, this package is
currently locked to revision 31655 (April 19, 2010), but this revision will be
updated on a regular basis to the latest available BFL trunk. This ROS package
does not modify BFL in any way, it simply provides a convenient way to download
and compile the library, because BFL is not available from an OS package
manager. This ROS package compiles BFL with the Boost library for matrix
operations and random number generation.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Thu Mar 23 2017 Wim Meeussen <meeussen@willowgarage.com> - 0.7.0-0
- Autogenerated by Bloom

